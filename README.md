# raspberryServer

# starting Server

source env/bin/activate
# to start virtual enviroment

# for first time you should execute command below to create fisrt database table
python ini_db.py

# start server
export FLASK_APP=app
flask run