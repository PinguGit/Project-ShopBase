from flask import Flask
import mysql.connector

def db_connect():
    return mysql.connector.connect(        
        #host="172.16.182.178",

        host ="172.16.182.181",
        user="power_user",
        password="adrian_stinkt",
        database="shopsystem"
    )
