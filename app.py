import sqlite3
import serial
import string
import time
from flask import Flask, render_template, url_for, redirect

def get_db_connection():
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn

app = Flask(__name__)

@app.route('/')
def index():
        conn = get_db_connection()
        logs = conn.execute('SELECT * FROM logs').fetchall()
        conn.close()
        return render_template('index.html', logs=logs)

@app.route('/delete/')
def delete():
	conn = get_db_connection()
	conn.execute('DELETE FROM logs')
	conn.commit()
	conn.close()
	return redirect(url_for('index'))
