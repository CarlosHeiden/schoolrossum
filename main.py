import socket
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'banco/base_dados.sqlite3')
app.config['SECRET_KEY'] = '123456'
db = SQLAlchemy(app)


from view import *


def get_server_ip():
    hostname = socket.gethostname()
    server_ip = socket.gethostbyname(hostname)
    return server_ip


#server_ip = get_server_ip()
#print(server_ip)
#app.run(host=f"{server_ip}", port=80, debug=True)

if __name__ == '__main__':
    app.run(debug=True)


