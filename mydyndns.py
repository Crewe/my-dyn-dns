#mydyndns.py

import json
import cgi
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, IPAddress
from flask import Flask, request, redirect
from flask import jsonify, make_response


app = Flask(__name__)
app.secret_key = 'APP_SECRET_KEY'
engine = create_engine(config.connectionString())
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

API_KEY = 'MAKE_IT_GOOD'


@app.route('/ip', methods=['POST'])
def setIpAddress():
    if request.form['key'] == API_KEY:
        try:
            addIpAddress(request.form['ip'])
        except:
            response = make_response('Bad IP address.', 400)
            response.headers['Content-Type'] = 'text/plain'
        response = make_response('OK', 200)
        response.headers['Content-Type'] = 'text/plain'
    else:
        response = make_response('', 400)
        response.headers['Content-Type'] = 'text/plain'
    return response


@app.route('/server')
def server():
    ip = getIpAddress()
    return redirect('http://' + ip.ipv4)


def addIpAddress(ip):
    ip_addr = IPAddress(ipv4=ip)
    session.add(ip_addr)
    session.commit()
    return None


def getIpAddress():
    ip_addr = session.query(IPAddress).order_by(IPAddress.id.desc()).first()
    return ip_addr


if __name__ == '__main__':
    app.debug = False 
