import streamlit as st
import pickle
import pandas as pd
import requests

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=42773df8e2287ba37521250749c211e6&language=en-US'.format(movie_id))
#     data = response.json()
#     return data['poster_path']
def recomended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open("movies_dict.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))
movies = pd.DataFrame(movies_dict)
st.title("Movie Recommender System")
selected_move = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recomend'):
    recommendations = recomended(selected_move)
    for i in recommendations:
        st.write(i)