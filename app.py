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
        bme_data = conn.execute('SELECT * FROM bme_data ORDER BY id DESC LIMIT 10').fetchall()
        conn.close()
        return render_template('index.html', bme_data=bme_data)

@app.route('/delete/')
def delete():
	conn = get_db_connection()
	conn.execute('DELETE FROM bme_data')
	conn.commit()
	conn.close()
	return redirect(url_for('index'))
