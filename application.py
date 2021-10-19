from flask import Flask
from flask import render_template

application = Flask(__name__, static_folder='static', template_folder='templates')


@application.route('/', methods=["GET"])
def hello_world():  # put application's code here
    return 'Hello World!'


@application.errorhandler(404)
def page_not_found(error):
    return '404', 404


@application.errorhandler(403)
def permission_denied(error):
    return '403', 403


@application.route('/users/<str:username>')
def show_users(username):
    return username


if __name__ == '__main__':
    application.run()
