from os import path
import sqlite3

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")
def create_post(name, content):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()
    
def get_posts():
    con =sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts