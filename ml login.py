from flask import Flask,render_template,request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def user():
    return render_template('loginpage.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/home')
def home():
    return render_template('home.html')

conn=mysql.connector.connect(host="localhost",user="root",password="Avishek2001@",database="user")
cursor=conn.cursor()

@app.route('/login_validation',methods=['post'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    cursor.execute("""SELECT * FROM `info` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        return render_template('home.html')
    else:
        return render_template('loginpage.html')

@app.route('/add_user',methods=['post'])
def add_user():
    user_name=request.form.get('user_name')
    email=request.form.get('email')
    password=request.form.get('password')
    cursor.execute("""INSERT INTO `info` (`username`,`email`,`password`) VALUES ('{}','{}','{}')""".format(user_name,email,password))
    conn.commit()
    return render_template('home.html')

if __name__ =='__main__':
  app.run(debug=True)