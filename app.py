from flask import Flask
from dao import clienteDao

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

from routes import *

if __name__ == '__main__':
    app.run(debug=True)