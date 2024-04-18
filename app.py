import streamlit as st
import pickle
import requests


def fetch_poster(movie_name):
    params = {
        "apikey": "a4ae81c9",
        "t": movie_name
    }
    response = requests.get("http://www.omdbapi.com/", params=params)
    data = response.json()
    print(data)
    if "Poster" in data:
        return data["Poster"]
    else:
        return []

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

st.header("Movie Recommender System")

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster("Spider man"),
    fetch_poster("The Shawshank Redemption"),
    fetch_poster("oppenheimer"),
    fetch_poster("The Godfather"),
    fetch_poster("A Beautiful Mind"),
    fetch_poster("Interstellar"),
    fetch_poster("Dune: Part Two"),
]


imageCarouselComponent(imageUrls=imageUrls, height=200)
selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:13]:
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies.iloc[i[0]].title))
    return recommend_movie, recommend_poster

def renderColumns():
    movie_name, movie_poster = recommend(selectvalue)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[0]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)

    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[1]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)

    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[2]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)

    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[3]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)

def renderColums1():
    movie_name, movie_poster = recommend(selectvalue)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.text(movie_name[4])
        st.image(movie_poster[4])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[4]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)

    with col2:
        st.text(movie_name[5])
        st.image(movie_poster[5])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[5]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)

    with col3:
        st.text(movie_name[6])
        st.image(movie_poster[6])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[6]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)

    with col4:
        st.text(movie_name[7])
        st.image(movie_poster[7])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[7]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)


if st.button("Show Recommend"):
    renderColumns()
    renderColums1()

    movie_name, movie_poster = recommend(selectvalue)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.text(movie_name[8])
        st.image(movie_poster[8])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[8]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)

    with col2:
        st.text(movie_name[9])
        st.image(movie_poster[9])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[9]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)

    with col3:
        st.text(movie_name[10])
        st.image(movie_poster[10])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[10]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)

    with col4:
        st.text(movie_name[11])
        st.image(movie_poster[11])
        html = f'<a href="http://www.omdbapi.com/?t={movie_name[11]}&apikey=a4ae81c9">View Details</a>'
        st.write(html, unsafe_allow_html=True)
