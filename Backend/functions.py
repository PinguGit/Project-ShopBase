from flask import Flask
import mysql.connector

def db_connect():
    return mysql.connector.connect(        
        host="172.16.182.160",
        #host ="127.0.0.1",
        user="power_user",
        password="adrian_stinkt",
        database="shopsystem"
    )
