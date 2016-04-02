import sys
# Adds site app to python's path so imports can be used
sys.path.insert(0, '/var/www/app_dir')
from mydyndns import app as application
