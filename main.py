
from flask import Flask, request, url_for, render_template


app = Flask(__name__)

@app.route('/')
def landing_page():
	return render_template('landing_page.html')

@app.route('/')
def user_login():
    user = users.get_current_user()
    if user:
        nickname = user.nickname()
        logout_url = users.create_logout_url('/')
        greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
            nickname, logout_url)
    else:
        login_url = users.create_login_url('/')
        greeting = '<a href="{}">Sign in</a>'.format(login_url)

    return '<html><body>{}</body></html>'.format(greeting)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
