# Python modules
import logging
from flask import Flask, request, url_for, render_template
import jinja2
import os
import json

# Google modules
from google.appengine.api import users
from google.appengine.api import urlfetch


app = Flask(__name__)

# some metadata to make available to all sites and functions
app.vars = {}
#app['APPLICATION_ID'] = os.environ['APPLICATION_ID']
#app['CURRENT_VERSION_ID'] = os.environ['CURRENT_VERSION_ID']
#app['SERVER_SOFTWARE'] = os.environ['SERVER_SOFTWARE']
#app['AUTH_DOMAIN'] = os.environ['AUTH_DOMAIN']


@app.route('/')
def home_page():
    user = users.get_current_user()
    if user:
        nickname = user.nickname()
        login_logout_url = users.create_logout_url('/')
        ### call an API ###
        url = 'https://alpha-endpoints1-dot-machine-learning-backend.appspot.com/_ah/api/statisticaltests/v1/ttest?_sm_au_=iVVn5Qn6JqZj24Wr'
        #url = 'http://www.google.com/humans.txt'
        result = urlfetch.fetch(url, validate_certificate=True, follow_redirects=False)
        if result.status_code == 200:
            #api_result = json.loads(result.content)
            # manipulate the response
            api_result = str(type(result.content))
        else:
            api_result = 'API_ERROR'
    else:
    	nickname = 'Unknown User'
        login_logout_url = users.create_login_url('/')
        api_result = None

    return render_template('landing_page.html', user = user, nickname = nickname, login_logout_url = login_logout_url, app_id = os.environ['APPLICATION_ID'], version_id = os.environ['CURRENT_VERSION_ID'], auth_domain = os.environ['AUTH_DOMAIN'], server_software = os.environ['SERVER_SOFTWARE'], api_result=api_result)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
