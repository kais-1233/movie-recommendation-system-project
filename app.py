import streamlit as st
import pickle
import pandas as pd
import base64

# --------------------- Set Background and Styling ---------------------
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{b64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    
streA
    /* Selectbox dropdown area (fix white text issue) */
    .stSelectbox div[data-baseweb="select"] * {{
        color: black !important;
        text-shadow: none !important;
        background-color: white !important;
    }}

    /* Selected value (inside the selectbox) */
    .stSelectbox div[data-baseweb="select"] > div {{
        color: black !important;
    }}

    /* Button styling */
    .stButton>button {{
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.6em 1.5em;
        border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        transition: all 0.2s ease-in-out;
    }}
    .stButton>button:hover {{
        background-color: #FF7F7F;
        color: black;
        transform: scale(1.05);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call background before UI
set_background("logos.png")

# --------------------- Recommend Function ---------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

# --------------------- Load Data ---------------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --------------------- Streamlit UI ---------------------
st.title('🎬 Movie Recommender System')
st.markdown('**By Kais Khan**')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    st.subheader("🎥 Recommended Movies:")
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(f"👉 {i}")
