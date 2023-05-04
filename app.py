#!/usr/bin/python
import os
import pymysql

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# mysql://username:password@host:port/database_name
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

@app.route("/")
def index():
    db.session.query(text('1')).from_statement(text('SELECT 1')).all()
    return "<h1>It works.</h1>Version: {}".format(os.environ['VERSION'])
    #try:
    #    db.session.query(text('1')).from_statement(text('SELECT 1')).all()
    #    return "<h1>It works.</h1>Version: {}".format(os.environ['VERSION'])
    #except:
    #    return "<h1>Something is broken.</h1>Version: {}".format(os.environ['VERSION'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)