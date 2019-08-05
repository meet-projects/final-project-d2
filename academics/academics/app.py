from database import *
from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def homepage():
	ls = session.query(Product).all()
	return render_template("index.html",ls=ls)

@app.route('/store')
def store():
	ls = session.query(Product).all()
	return render_template("courses.html",ls =ls)

@app.route('/contact')
def contact():
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


if __name__ == '__main__':
   app.run(debug = True)
