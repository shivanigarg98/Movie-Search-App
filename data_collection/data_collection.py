import requests
import time
import pandas as pd
from credentials import api_key

def collect_data(skip_step=False):
    if skip_step:
        print("Skipping Data Collection Step")
        return True
    try:
        base_url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page='
        
        response = requests.get(base_url)
        
        # Fetching all pages of popular movies
        page_number = 1
        all_movies = []
        movie_dict_list = []
        df = pd.DataFrame()
        count = 0
        movies_to_collect = 100  # Limit the collection to 100 movies

        while len(all_movies) < movies_to_collect:
            try:
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
                }
                response = requests.get(f"{base_url}{page_number}", headers=headers)
                if response.status_code != 200:
                    continue
                movie_data = response.json()
                
                if movie_data['results']:
                    all_movies.extend(movie_data['results'])
                    page_number += 1
                    count += len(movie_data['results'])
                else:
                    break
                time.sleep(3)
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                print("Retrying...")
                time.sleep(3)  # Wait for a second before retrying
                continue

            if len(all_movies) >= movies_to_collect:
                break  # Break the loop if already collected the desired number of movies

        movie_count = 0
        for movie in all_movies[:movies_to_collect]:  # Iterate only over the required number of movies
            try:
                additional_info_url = f"https://api.themoviedb.org/3/movie/{movie['id']}?api_key={api_key}&language=en-US"
                additional_info_response = requests.get(additional_info_url)
                
                additional_info_data = additional_info_response.json()
                genres = ', '.join([genre['name'] for genre in additional_info_data['genres']])
                average_vote = additional_info_data['vote_average']
                runtime = additional_info_data['runtime']

                # Create dictionary and append movie details
                movie_dict = {
                    "id": movie['id'],
                    "title": movie['title'],
                    "overview": movie['overview'],
                    "release_date": movie['release_date'],
                    "popularity": movie['popularity'],
                    'genres': genres,
                    "average_vote": average_vote,
                    "runtime": runtime,
                    "poster_path": movie["poster_path"]
                }
                movie_dict_list.append(movie_dict) 

                movie_count += 1
                if movie_count == movies_to_collect:
                    break  # Break the loop when the desired count is reached

            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                print("Retrying...")
                time.sleep(3)  # Wait for a second before retrying
                continue

        df = pd.DataFrame(movie_dict_list)
        df.to_csv('data/movie_tmdb_file_100.csv')

        print("Data Successfully collected and saved as a CSV!")
        return True
    except Exception as e:
        print(f"Data Collection is causing an error: {e}")
        return False


