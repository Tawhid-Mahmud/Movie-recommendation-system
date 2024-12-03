import streamlit as st
import pandas as pd
import requests
import pickle

# Load the precomputed movie data and cosine similarity matrix from a pickle file
with open('movies.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

def get_recommendations(title, cosine_sim=cosine_sim):
    # Find the index of the movie that matches the title
    idx = movies[movies['title'] == title].index[0]
    
    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11] # getting the top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the top 10 most similar movies
    return movies['title'].iloc[movie_indices]

def fetch_poster(movie_id):
    # Define the API key and URL for fetching movie posters
    api_key = 'TMDB_API_KEY'  # replace with your TMDB API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    
    # Make a request to the API
    response = requests.get(url)
    
    # Parse the JSON response
    data = response.json()
    
    # Construct the full path to the movie poster
    poster_path = data['poster_path']
    full_path = f'https://image.tmdb.org/t/p/w500/{poster_path}'
    
    return full_path

# Set the title of the Streamlit app
st.title('Movie Recommender System')

# Create a dropdown menu for selecting a movie
selected_movie = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommendations = get_recommendations(selected_movie)
    st.write("Top 10 recommendations:")
    
    # create a 2x5 grid for the recommendations
    for i in range(0, 10, 5):
        cols = st.columns(5)
        for col, j in zip(cols, range(i, i+5)):
            if j < len(recommendations):
                movie_title = recommendations.iloc[j]
                movie_id = movies[movies['title'] == movie_title]['movie_id'].values[0]
                poster_url = fetch_poster(movie_id)
                with col: 
                    st.image(poster_url, width=130)
                    st.write(movie_title)
    
