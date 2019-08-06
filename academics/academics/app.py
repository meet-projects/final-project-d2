from database import *
from flask import Flask, render_template,url_for,request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'integratedplants@gmail.com'
app.config['MAIL_PASSWORD'] = 'shekuisking123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/', methods=['GET','POST'])
def homepage():
	if request.method =='POST':
		msg = Message(request.form['name'] + " " + request.form['family'], sender = 'integratedplants@gmail.com', recipients = ['integratedplants@gmail.com'])
   		msg.html = "<p>" + request.form['prod'] + "</p> <br> <p>" + request.form['quan'] +"</p> <br> <p>" + request.form['email'] + "</p> <br> <p>" + request.form['tel'] + "</p>"
   		mail.send(msg)
	ls = session.query(Product).all()
	return render_template("index.html",ls=ls)

@app.route('/store')
def store():
	ls = session.query(Product).all()
	return render_template("courses.html",ls =ls)

@app.route('/contact',methods=['GET','POST'])
def contact():
	if request.method == 'POST':
		msg = Message(request.form['name'] + " " + request.form['family'], sender = 'integratedplants@gmail.com', recipients = ['integratedplants@gmail.com'])
   		msg.html = "<p>" + request.form['message'] + "</p> <br> <p>" + request.form['email'] + "</p> <br> <p>" + request.form['tel'] + "</p>"
   		mail.send(msg)

	return render_template("contact.html")

@app.route('/aboutus')
def about():
	return render_template("about.html")

@app.route('/stories')
def stories():
	return render_template("read.html")

@app.route('/product/<int:product_id>')
def display_product(product_id):
	product = query_by_id(product_id)
	return render_template("course-single.html", product = product)

@app.route('/buy')
def buy():
	ls = session.query(Product).all()
	return render_template("buy.html",ls = ls)

if __name__ == '__main__':
   app.run(debug = True)
