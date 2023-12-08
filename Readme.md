# Movie Search App 🔍

This Movie Search App allows users to search for movies and get detailed information about them.

The app has 4 pages : Home, About, Data Description, Search

Usage : Go to Search Page in the left sidebar to search for movies

![image-20231208152323501](blob:https://medium.com/ca5d981c-96b5-48a5-9c59-4125febb17b8)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- User-friendly interface to search for movies by title.
- Display detailed information about selected movies.
- The API's are used from https://www.themoviedb.org/ (You must generate your own api key to make it work on local)

## Installation

To run this app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Movie-Search-App.git
   ```

2. Install dependencies:

   ```bash
   # Navigate to the project directory
   cd Movie_Search_App
   
   # Install required packages or dependencies
   # You may need Python 3 installed. Use a virtual environment if desired.
   # Example: Create a virtual environment
   python -m venv myenv
   
   # Activate the virtual environment (Command may vary based on OS)
   # On Windows:
   venv\Scripts\activate
   # On macOS and Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. Start the application:

   ```bash
   # Run the application
   python main.py
   ```

4. Access the app:

   Once the app is running, access it through a web browser using the following URL:

   ```
   http://localhost:8501  # Adjust the port number if necessary
   ```

## Usage

- Enter a movie title in the search bar and press 'Get Info' to get information about that movie.
- Click on a movie to view its detailed information.

## Technologies Used

- Python
- Streamlit (or any other libraries/frameworks used)
- Sqllite
