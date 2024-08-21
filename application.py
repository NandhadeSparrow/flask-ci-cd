from flask import Flask


application = Flask(__name__)
app = application

@app.route('/')
def hello_world():
    return 'hey bruh wassup...'


if __name__ == '__main__':
    app.run()