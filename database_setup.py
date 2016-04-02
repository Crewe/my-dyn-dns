# database_setup.py
# Database configuration file for the ORM
#

import os
import sys
import config
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class IPAddress(Base):
    # Table to describe the users of the system
    __tablename__ = 'ipaddress'
    id = Column(Integer, primary_key=True)
    ipv4 = Column(String(15), nullable=False)
    ipv6 = Column(String(45))

    @property
    def serializable(self):
        return {
            'id': self.id,
            'ipv4': self.name,
        }


engine = create_engine(config.connectionString())
Base.metadata.create_all(engine)
