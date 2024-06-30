import mysql.connector
from mysql.connector import errorcode

config = {
    "user":"root",
    "password":"Omnisiah851048!",
    "host":"127.0.0.1",
    "database":"movies",
    "raise_on_warnings":True
}
try:
    db = mysql.connector.connect(**config)
    print("\n DATABASE USER {} CONNECTED TO MYSQL HOST{} WITH DATABASE{}".format(config["user"],config["host"],config["database"]))
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("THE SUPPLIED USERNAME OR PASSWORD ARE INVALID")
    elif er.errno == errorcode.ER_BAD_DB_ERROR:
        print("THE SUPPLIED DATABASE DOES NOT EXIST")
    else:
        print(err)

finally:
    db.close()
