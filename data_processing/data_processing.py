"""File to Process data"""

import pandas as pd

def process_data(skip_step=False):
    if skip_step:
        print("Skipping Data Processing Step")
        return True
    try:
        df = pd.read_csv("/data/movie_tmdb_file_100.csv") 
        df = df.iloc[0:100,:]
        df.drop(['Unnamed: 0'],axis=1,inplace=True)
        #completing url to access thumbnail link
        site_thumbnail_url = "https://image.tmdb.org/t/p/w500"
        df['poster_path'] = df['poster_path'].apply(lambda  x : site_thumbnail_url + x)

        ## converting release date to datetime
        df['release_date'] = pd.to_datetime(df['release_date'])

        ## rounding of popularity, avg_vote  to 2 decimal
        df['popularity'] = df['popularity'].round(2)
        df['average_vote'] = df['average_vote'].round(2)
        df.to_csv('data/processed_movie_tmdb_100.csv')
        print("Data Processing Completed!")
        return True
        
    except Exception as e:
        print(f"Data Processing is causing error : {e}")
        return False
