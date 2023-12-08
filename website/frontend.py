import requests
import streamlit as st


# Streamlit UI for interacting with Flask routes
st.title("Movie Search App")

# Flask routes URLs
flask_url = 'http://localhost:5000'

page = st.sidebar.selectbox("Select a page", ['Home', 'About', 'Data Description', 'Search'])

def get_all_movie_titles():
    url = f'{flask_url}/all_movie_titles'  # Flask server URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('movie_titles', [])
    return []

# Function to retrieve movie information based on the selected title
def get_movie_info(title):
    url = f'{flask_url}/get_movie_info/{title}'  # Include the movie title in the URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {'error': 'Movie not found!'} 

if page == 'Home':
    st.write("Welcome to Movie Search App!")

elif page == 'About':
    st.write("This app gives you the information about the movie by selecting it's name")

elif page == 'Data Description':
    st.write("Overview : Get the Overview of movie")
    st.write("Release Date : Get the Release Date of movie (YY-MM-DD)")
    st.write("Popularity : The Popularity Score of the movie")
    st.write("Genres : Genre for the Movie")
    st.write("Average Vote : Voted by watchers out of 10")
    st.write("Runtime : Runtime of the movie in minutes")

elif page == 'Search':
    st.write("Search About Movie :")


    st.title("Movie Information Viewer")

    # List of available movies (you can replace this with your movie titles)
    movie_titles = get_all_movie_titles()  # Add your movie titles here

    # Dropdown to select a movie
    selected_movie = st.selectbox("Select a movie", movie_titles)

    if st.button("Get Movie Info"):
        # Check if a movie is selected
        if selected_movie:
            # Retrieve movie information
            movie_data = get_movie_info(selected_movie)
            # Display movie information
            if 'error' in movie_data:
                st.error(movie_data['error'])
            else:
                if movie_data['poster_path']:
                    st.write("**Poster:**")
                    st.image(movie_data['poster_path'],width=200)
                else:
                    st.write("**Poster:** Poster not available")
                st.write("**Overview:**", movie_data['overview'])
                st.write("**Release Date:**", movie_data['release_date'])
                st.write("**Popularity:**", movie_data['popularity'])
                st.write("**Genres:**", movie_data['genres'])
                st.write("**Average Vote:**", movie_data['average_vote'])
                st.write("**Runtime:**", movie_data['runtime'])
                
                    