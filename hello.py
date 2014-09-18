from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():

    return 'Hello NICE!'

@app.route('/name')
def print_name():
    return '不错，你很厉害！'

if __name__ == '__main__':
    app.run()
