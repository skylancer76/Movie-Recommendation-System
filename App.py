{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "728920e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import streamlit as st\n",
    "import requests\n",
    "\n",
    "def fetch_poster(movie_id):\n",
    "    url = \"https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US\".format(movie_id)\n",
    "    data = requests.get(url)\n",
    "    data = data.json()\n",
    "    poster_path = data['poster_path']\n",
    "    full_path = \"https://image.tmdb.org/t/p/w500/\" + poster_path\n",
    "    return full_path\n",
    "\n",
    "def recommend(movie):\n",
    "    index = movies[movies['title'] == movie].index[0]\n",
    "    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])\n",
    "    recommended_movie_names = []\n",
    "    recommended_movie_posters = []\n",
    "    for i in distances[1:6]:\n",
    "        # fetch the movie poster\n",
    "        movie_id = movies.iloc[i[0]].movie_id\n",
    "        recommended_movie_posters.append(fetch_poster(movie_id))\n",
    "        recommended_movie_names.append(movies.iloc[i[0]].title)\n",
    "\n",
    "    return recommended_movie_names,recommended_movie_posters\n",
    "\n",
    "\n",
    "st.header('Movie Recommender System')\n",
    "movies = pickle.load(open('movie_list.pkl','rb'))\n",
    "similarity = pickle.load(open('similarity.pkl','rb'))\n",
    "\n",
    "movie_list = movies['title'].values\n",
    "selected_movie = st.selectbox(\n",
    "    \"Type or select a movie from the dropdown\",\n",
    "    movie_list\n",
    ")\n",
    "\n",
    "if st.button('Show Recommendation'):\n",
    "    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)\n",
    "    col1, col2, col3, col4, col5 = st.beta_columns(5)\n",
    "    with col1:\n",
    "        st.text(recommended_movie_names[0])\n",
    "        st.image(recommended_movie_posters[0])\n",
    "    with col2:\n",
    "        st.text(recommended_movie_names[1])\n",
    "        st.image(recommended_movie_posters[1])\n",
    "\n",
    "    with col3:\n",
    "        st.text(recommended_movie_names[2])\n",
    "        st.image(recommended_movie_posters[2])\n",
    "    with col4:\n",
    "        st.text(recommended_movie_names[3])\n",
    "        st.image(recommended_movie_posters[3])\n",
    "    with col5:\n",
    "        st.text(recommended_movie_names[4])\n",
    "        st.image(recommended_movie_posters[4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "5e84699e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
