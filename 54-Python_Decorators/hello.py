from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'Bye'

# set FLASK_APP=hello.py
if __name__ == "__main__":
    app.run()
