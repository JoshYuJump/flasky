#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask_db_app import app
from flask_db_sqlite_models import User
import sqlite3

manager = Manager(app)

# python flask_db_sqlite.py hello
@manager.command
def hello():
    print "hello world!"

# python flask_db_sqlite.py hello_world -m china
@manager.option('-m', '--msg', dest='msg_val', default='world')
def hello_world(msg_val):
    print 'hello ' + msg_val


@manager.command
def init_db():
    sql = "create table user(id INT, name TEXT)"
    conn = sqlite3.connect('flask_db_sqlite.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


@manager.command
def save():
    user = User(1, 'jack')
    user.save()


@manager.command
def query_all():
    users = User.query()
    for user in users:
        print user


if __name__ == '__main__':
    manager.run()    