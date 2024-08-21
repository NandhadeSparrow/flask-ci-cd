from flask import Flask


application = Flask(__name__)
app = application

@app.route('/')
def hello_world():
    return 'ssup bruh'


if __name__ == '__main__':
    app.run()