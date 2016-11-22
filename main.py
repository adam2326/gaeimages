import logging
from flask import Flask, request, url_for, render_template
from google.appengine.api import users
import jinja2
import os


app = Flask(__name__)

# some metadata to make available to all sites and functions
app.vars = {}
app['APPLICATION_ID'] = os.environ['APPLICATION_ID']
app['CURRENT_VERSION_ID'] = os.environ['CURRENT_VERSION_ID']
app['SERVER_SOFTWARE'] = os.environ['SERVER_SOFTWARE']
app['AUTH_DOMAIN'] = None


@app.route('/')
def home_page():
    user = users.get_current_user()
    if user:
        nickname = user.nickname()
        login_logout_url = users.create_logout_url('/')
        app['AUTH_DOMAIN'] = os.environ['AUTH_DOMAIN']
    else:
    	nickname = 'Unknown User'
        login_logout_url = users.create_login_url('/')

    return render_template('landing_page.html', user = user, nickname = nickname, login_logout_url = login_logout_url, app_id = app['APPLICATION_ID'], version_id = app['CURRENT_VERSION_ID'], auth_domain = app['AUTH_DOMAIN'], server_software = app['SERVER_SOFTWARE'])


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
