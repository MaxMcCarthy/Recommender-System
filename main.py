from flask import Flask

application = Flask(__name__)
application.secret_key = 'super secret string'  # Change this!
application.debug = True


@application.route('/')
def home_page():
    return 'Hello World!'


if __name__ == '__main__':
    application.run()

