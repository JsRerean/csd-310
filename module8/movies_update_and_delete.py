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
    cursor = db.cursor()

    def showFilms(cursor,title):
        cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film " 
                       "INNER JOIN genre ON film.genre_id = genre.genre_id "
                       "INNER JOIN studio ON film.studio_id = studio.studio_id"
                       )
        films = cursor.fetchall()
        print("\n   --- {}  ---".format(title))
        for film in films:
            print("\nFilm Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}".format(film[0],film[1],film[2],film[3]))
    showFilms(cursor,"DISPLAYING FILMS")#pre update output

    cursor.execute("UPDATE film SET genre_id=1 WHERE film_id=2")
    showFilms(cursor,"DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror ")#post update output
    
    cursor.execute("INSERT INTO film(film_name,film_releasedate,film_runtime,film_director,studio_id,genre_id) "#insert
                   "VALUES('Oppenhiemer','2023','180','Christopher Nolan',(SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'),(SELECT genre_id FROM genre WHERE genre_name = 'Drama'))"
                   )
    showFilms(cursor,"DISPLAYING FILMS AFTER INSERT - Added Oppenheimer")

    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
    showFilms(cursor,"DISPLAYING FILMS AFTER DELETION - Deleted Gladiator")

except mysql.connector.Error as err: #error handler
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("THE SUPPLIED USERNAME OR PASSWORD ARE INVALID")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("THE SUPPLIED DATABASE DOES NOT EXIST")
    else:
        print(err)

finally:
    db.close()