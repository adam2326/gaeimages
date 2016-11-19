import logging
from flask import Flask, request, url_for, render_template
from google.appengine.api import users


app = Flask(__name__)


@app.route('/')
def home_page():
    user = users.get_current_user()
    if user:
        nickname = user.nickname()
        login_logout_url = users.create_logout_url('/')
    else:
    	nickname = 'Unknown User'
        login_logout_url = users.create_login_url('/')

    return render_template('landing_page.html', nickname = nickname, login_logout_url = login_logout_url)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
