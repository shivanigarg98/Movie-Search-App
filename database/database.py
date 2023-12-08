"""File for Database"""

import sqlite3
import pandas as pd

# Create a SQLite connection
def create_db(skip_step=False):
    if skip_step:
        print("Skipping Database Step")
        return True
    try:
        conn = sqlite3.connect('tmdb_movie_100.db')
        # Convert the data to a Pandas DataFrame
        df = pd.read_csv('data/processed_movie_tmdb_100.csv')
        

        # Store the data in the SQLite database
        df.to_sql('movie', conn, if_exists='replace', index=False)

        # # Close the connection
        conn.commit()
        conn.close()
        print("Database Creation Done!")
        return True
    except Exception as e:
        print(f"Database is causing error : {e}")
        return False

