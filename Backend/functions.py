from flask import Flask
import mysql.connector

def db_connect():
    return mysql.connector.connect(        
        host="172.16.182.142",
        user="power_user",
        password="adrian_stinkt",
        database="shopsystem"
    )

def delete_by_obejct(obj):
    return(type(obj).__name__)



def delete():
    ""

