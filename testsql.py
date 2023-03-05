# Implement a simple python script using psycopg2 and argparse libraries.
# The script will display the movies from your database based on the user’s preferences.
# The user should be able to perform the following:
# Check whether the movie with specific name is among the top 250 movies.
# If so - display the release year of the movie and the imdb rating
# Display the user all the movies with imdb rating higher than the one provided by the user.
import pprint

import psycopg2

with psycopg2.connect(host="localhost",
                        port=5432,
                        database="imdb",
                        user="postgres",
                        password="danick92") as conn:
    def find_movie(movie_name):
        with conn.cursor() as cur:

            sql = f"select movie_name , release_date , rating from imdb_top it where movie_name = {movie_name};"
            cur.execute(sql)
            result = cur.fetchone()
        return result


    def find_movies_by_rating(rate):
        with conn.cursor() as cur:
            sql = f"select movie_name, rating from imdb_top it where rating > {rate};"
            cur.execute(sql)
            result = cur.fetchall()
        return result

res = find_movies_by_rating(8)
pprint.pprint(res)

res1 = find_movie("Spider")
print(res1)




