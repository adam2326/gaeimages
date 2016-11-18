
from flask import Flask, request, url_for, render_template


app = Flask(__name__)

@app.route('/')
def landing_page():
	return render_template('landing_page.html')
