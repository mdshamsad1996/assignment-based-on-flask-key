"""
Contained the common setting and obj which is used by most of other module 
"""

from flask import Flask
from flask_mysqldb import MySQL
from src.hash_utils import HashUtils

hash_utils_obj = HashUtils()

app = Flask(__name__)

app.config['host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'shamsad@123'
app.config['MYSQL_DB'] = 'reg_mngmnt_schedule_event'

mysql = MySQL(app)

from src import routes
