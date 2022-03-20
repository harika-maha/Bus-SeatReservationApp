from flask import Flask, redirect, session, url_for, render_template, request
import mysql.connector
from datetime import date

mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="busApp")
cur = mydb.cursor()

app = Flask(__name__)

session = {'loggedin': False, 'email': '', 'name': ''}
busdict = {}
busarray = []
seatsBooked = 0

@app.route('/', methods=["POST", "GET"])

def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])

def login():
    msg = ''
    if 'Email' in request.form and 'Password' in request.form:
        email = request.form["Email"]
        password = request.form["Password"]
        cur.execute('SELECT * FROM login WHERE email = %s AND password = %s', (email, password))
        account = cur.fetchone()
        print(account)
        # for account in accounts:
        if account:
            session['loggedin'] = True
            session['email'] = account[0]
            session['name'] = account[2]
            print(session['email'])
            return redirect(url_for('buses'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg = msg)
        
            
@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template('register.html')

@app.route('/registerResult', methods=["GET","POST"])
def registerResult():
    msg = ''
    email = request.form["email"]
    password = request.form["pass"]
    name = request.form["name"]
    cur.execute('SELECT * FROM login WHERE email = %s', (email,))
    account = cur.fetchone()
    if account:
        msg = "Account Already Exists"
    else:
        cur.execute("INSERT INTO LOGIN VALUES('{}', '{}','{}')".format(email, password, name))
        mydb.commit()
        msg = "Registered Successfully"
    return render_template('register.html',regmsg = msg)

@app.route('/buses', methods=["GET","POST"])
def buses():
    busarray = []
    cur.execute("SELECT * FROM buses")
    buses = cur.fetchall()
    # print(buses)
    # print(buses[0][0])
    for i in range(len(buses)):
        src = buses[i][0]
        dest = buses[i][1]
        avail = buses[i][2]
        price = buses[i][3]
        today = date.today()
        busid = buses[i][5]
        busdict = {'src': src, 'dest': dest, 'avail': avail, 'price': price, 'date': today, 'busid':busid}
        busarray.append(busdict)
    print(busarray)
    return render_template('buses.html', value = buses, busarray = busarray)


seatsBooked = 0
@app.route('/busBooked', methods=['POST', 'GET'])
def busBooked():
    msg = ''
    cur.execute('SELECT busid FROM buses')
    busids = cur.fetchall()
    print(busids)
    for busid in busids:
    #     print(busid[0])
    #     print(request.form)
      if str(busid[0]) in request.form:
          seats = request.form.get("seats")
          print(seats)
          seatsBooked = seats
        #   cur.execute('UPDATE buses SET avail = avail-{} WHERE busid={}'.format(seats,busid[0]))
        #   mydb.commit()
          cur.execute("SELECT * FROM buses WHERE busid={}".format(busid[0]))
          bus = cur.fetchone()
          print(bus)
          name = session['name']
          src = bus[0]
          dest = bus[1]
          date = bus[4]
          price = bus[3]
          avail = bus[2]
          if(avail < int(seats)):
              cur.execute('UPDATE buses SET avail = {} WHERE busid={}'.format(avail,busid[0]))
              return(render_template('buses.html', val="Required Tickets not Available for this Bus!"))
          else:
              cur.execute('UPDATE buses SET avail = avail-{} WHERE busid={}'.format(seats,busid[0]))
              mydb.commit()
              return render_template('ticket.html', src=src, dest=dest, date=date, price=price, name=name, seatsbooked=seatsBooked)
            
    #         msg = "BUSID = " + busid
    # return msg
    # cur.execute('SELECT * FROM buses WHERE busid = %d',(book))
    # bus = cur.fetchone()
    # print(bus)
   


@app.route('/logout')
def logout():
   session['loggedin'] = False
   session['email'] = ''
   # Redirect to login page
   return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)