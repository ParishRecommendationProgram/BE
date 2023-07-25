from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS()

from views import AI
app.register_blueprint(AI.bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()