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

@app.route('/get_data/')
def get_data():
	#open serial port
	ser = serial.Serial('/dev/ttyUSB0',9600)
	#check ls /dev/ttyUSBx for port
	serialdata = ser.readline()
	print(serialdata)
	deviceId = "Arduino"
	title = 'Temperature'
	conn = get_db_connection()
        conn.execute('INSERT INTO logs (devid, title, content) VALUES (?, ?, ?)',
                     (deviceId, title, serialdata.decode('utf-8')))
        conn.commit()
        conn.close()
	return redirect(url_for('index'))
