import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px 

#st.set_page_config(layout='wide')

st.title("Spotify Dataset")

data = pd.read_csv('data/data_w_genres.csv')


a1, a2 = st.columns(2)
# (Pie Chart of the artists) 
with a1:
    top_artist = data['artists'].value_counts().head(10)
    fig, ax = plt.subplots()
    ax.pie(top_artist, labels=top_artist.index, autopct='%1.1f%%')

    plt.title(f'Top 10 Artists')
    st.pyplot(fig)
    st.write("This Pie chart for the Top 10 Artists is key information that will help us focus on these particular artists work because most people listen to them and will help us in our Music Recommendation System project. ")

# (Heatmap)
with a2:
    df = data[['acousticness','danceability','duration_ms','energy','instrumentalness','liveness','loudness','speechiness','tempo','valence','popularity']]
    cor = df.corr()
    plt.figure(figsize=(10,8))
    sns.heatmap(data=cor, annot=True, cmap='coolwarm')
    st.pyplot()
    st.write("The heatmap is useful because it shows the correlation between the columns so if someone likes loudness we can suggest music that has high energy (for example).")
    st.set_option('deprecation.showPyplotGlobalUse', False)
