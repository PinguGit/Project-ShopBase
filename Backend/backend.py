from flask import Flask
import mysql.connector

app = Flask(__name__, static_url_path='', static_folder='static')

def db_connect():
    return mysql.connector.connect(        
        host="172.16.182.142",
        user="power_user",
        password="adrian_stinkt",
        database="shopsystem"
    )

db_connect()