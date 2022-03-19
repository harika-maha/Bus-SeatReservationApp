from crypt import methods
from flask import Flask, redirect, url_for, render_template, request
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="busApp")
cur = mydb.cursor()

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])

def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])

def login():
    email = request.form["Email"]
    password = request.form["Password"]
    cur.execute('SELECT * FROM login WHERE email = %s AND password = %s', (email, password))
    accounts = cur.fetchall()
    
    for account in accounts:
        if account:
            return 'Logged in successfully!'
        else:
            msg = 'Incorrect username/password!'
            return msg
            
@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template('register.html')

@app.route('/registerResult', methods=["GET","POST"])
def registerResult():
    email = request.form["email"]
    password = request.form["pass"]
    cur.execute('SELECT * FROM login WHERE email = %s', (email,))
    account = cur.fetchone()
    if account:
        return "Account Already Exists"
    else:
        cur.execute("INSERT INTO LOGIN VALUES('{}', '{}')".format(email, password))
        mydb.commit()
        return "Registered Successfully"

@app.route('/buses', methods=["GET","POST"])
def buses():
    cur.execute("SELECT * FROM buses")
    buses = cur.fetchall()
    return render_template('buses.html', value = buses)

# @app.route('')

if __name__ == "__main__":
    app.run(debug=True)