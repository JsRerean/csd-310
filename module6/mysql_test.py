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
    cursor = db.cursor()
    #query1
    cursor.execute("SELECT genre_name FROM genre") #moves cursor to genre table
    genres = cursor.fetchall()
    print ("GENRES:",genres)
    print()#for seperation of outputs
    #query2
    cursor.execute("SELECT studio_name FROM studio")#moves to studio table
    studios=cursor.fetchall()
    print("Studios:",studios)
    print()

    #query3
    cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120")
    film_under_two = cursor.fetchall()
    print("Films under 2 hours:",film_under_two)

    #query4
    cursor.execute("SELECT film_director, GROUP_CONCAT(film_name SEPARATOR ', ') AS films FROM film GROUP BY film_director")
    directors_and_films = cursor.fetchall()
    print("\nFilm Directors and Their Films:")
    for director, films in directors_and_films:
        print(f"Director: {director}")
        print(f"Films: {films}")
        print()

except mysql.connector.Error as err: #error handler
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("THE SUPPLIED USERNAME OR PASSWORD ARE INVALID")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("THE SUPPLIED DATABASE DOES NOT EXIST")
    else:
        print(err)

finally:
    db.close()

