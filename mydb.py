# Install Mysql on your computer
# http://dev.mysql.com/download/installer
# pip install mysql
# pip install mysql-connector-python
# pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = 'Mur1986at!'
)

# Prepare a cursor object

cursorObject = dataBase.cursor()

# Create a database 

cursorObject.execute("CREATE DATABASE dcrm")

print("Database Done!")