from database import *
from flask import Flask, render_template,url_for,request,redirect
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

@app.route('/admin',methods=['GET','POST'])
def admin():
	if request.method == 'POST':
		user = request.form['user']
		passw = request.form['pass']
		if user == '1' and passw == '1':
			return redirect(url_for('managment'))
	return render_template("admin.html")

@app.route('/managment', methods=['GET','POST'])
def managment():
	ls = session.query(Product).all()
	return render_template("managment.html", ls=ls)


@app.route('/product_managment/<int:product_id>', methods=['GET','POST'])
def display_product_managment(product_id):
	product = session.query(Product).filter_by(product_id=product_id).first()
	print(product)
	if request.method == 'POST':
		name = request.form['name']
		price = request.form['price']
		picture_path = request.form['path']

		if name != "":
			product.name=name
		if price != "":
			product.price=price
		if picture_path != "":
			product.picture_path=picture_path

		session.commit()
		ls = session.query(Product).all()
		return render_template('managment.html',ls = ls)
	return render_template("managment_product.html", product = product)

@app.route('/add_product',methods=['GET','POST'])
def add_product_page():
	if request.method == 'POST':
		name = request.form['name']
		picture_path = request.form['path']
		price = request.form['price']
		if name != "" and picture_path != "" and price != "" and type(price) is int:
			add_product(picture_path,name,price)
			return render_template("managment.html")
	return render_template("add_product.html")


if __name__ == '__main__':
   app.run(debug = True)
