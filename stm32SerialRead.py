import serial
import string
import time
import sqlite3
import struct

def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn

#open serial port
ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=1, bytesize=8, timeout=None)

#check ls /dev/tty* for ttyUSBx port
conn = get_db_connection()
while True :
	serialdata = ser.read(24)
	#serialData = ser.readline()
	#print(serialdata)
	temp, press, humid = struct.unpack('ddd',serialdata)
	conn.execute('INSERT INTO bme_data(temp, press, humid) VALUES (?, ?, ?)',(temp, press, humid))
	conn.commit()
conn.close()
