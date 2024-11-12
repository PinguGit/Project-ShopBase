from flask import Flask
import mysql.connector

def db_connect():
    return mysql.connector.connect(        
<<<<<<< HEAD
        # host="172.16.182.164",

        host ="127.0.0.1",
=======
        host="172.16.182.178",
        #host ="127.0.0.1",
>>>>>>> 4696ce5 (commit)
        user="power_user",
        password="adrian_stinkt",
        database="shopsystem"
    )
