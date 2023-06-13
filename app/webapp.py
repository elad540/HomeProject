from flask import Flask
import mysql.connector
from datetime import datetime

# Global counter
app = Flask(__name__)
counter = 0

# Database connection
connection = mysql.connector.connect(
    host="DB_HOST",
    user="user",
    password="password",
    database="database"
)

@app.route("/")
def increment_counter():
    global counter
    counter += 1

