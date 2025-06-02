import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values
similarity = pickle.load(open('Similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_names = st.selectbox(
    "How would you like to be contacted?",
    movies_list
)
if st.button("Recommend"):
    recommendations = recommend(selected_movie_names)
    for i in recommendations:
        st.write(i)

