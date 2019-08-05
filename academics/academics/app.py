from flask import Flask, render_template,url_for
app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("index.html")

@app.route('/store')
def store():
	return render_template("courses.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/aboutus')
def about():
	return render_template("about.html")

@app.route('/stories')
def stories():
	return render_template("read.html")


if __name__ == '__main__':
   app.run(debug = True)
