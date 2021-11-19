import serial
import string
import time
import sqlite3

def get_db_connection():
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn

#open serial port
ser = serial.Serial('/dev/ttyACM0',9600)
#check ls /dev/tty* for ttyUSBx port
conn = get_db_connection()
while True :
	serialdata = ser.readline()
	data = serialdata.split(" ")
        #BME280 temperature 20 C
        #INSERT INTO logs (id, title, content)
	conn.execute('INSERT INTO logs (devId, title, content) VALUES (?, ?, ?)',
             	     (data[0].decode('utf-8'), data[1].decode('utf-8'), data[2].decode('utf-8')+data[3].decode('utf-8')))
	conn.commit()
conn.close()
