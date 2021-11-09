# raspberryServer

# to start virtual enviroment
source env/bin/activate


# for first time you should execute command below to create fisrt database table
python ini_db.py

# start server
export FLASK_APP=app\n
flask run
