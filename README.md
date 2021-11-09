# raspberryServer

#Enable i2c to raspberry pi to get data from stm

 sudo raspi-config
 
 select interface options and enable i2c

# to start virtual enviroment
source env/bin/activate


# for first time you should execute command below to create fisrt database table
python ini_db.py

# start server
export FLASK_APP=app

flask run
