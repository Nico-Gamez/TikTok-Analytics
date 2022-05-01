#Imports Streamlit base dependency
import streamlit as st
#Import Pandas to load the data
import pandas as pd
#Import subprocess to run TikTok script from command line
from subprocess import call
#Import plotlib for visualization
import plotly.express as px

#Set page wide to wide
st.set_page_config(layout='wide')


#Create a Sidebar
st.sidebar.markdown("<div><img src='https://icones.pro/wp-content/uploads/2021/03/logo-icone-tiktok-simbolo.png' width=110 /><h1 style='display:inline-block'>TikTok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("")
st.sidebar.markdown("This dashboard allows you to collect a large amount of information from tags and with it you can analyze the trends on TikTok. 📊 ")
st.sidebar.markdown("Made with Python and Streamlit. 💻")
st.sidebar.markdown("👉To get started <ol><li>Enter the <strong>hashtag</strong> you wish to analyse<li>Hit <i><strong>Get Data</strong></i>.</li></li> <li>Get the analytics</li></ol>", unsafe_allow_html=True)

#Input
hashtag = st.text_input('Search the # you want here', value="")

df = pd.read_csv('TikTok_data.csv')
#Button
if st.button('Get My Data'):
    #Run get data function
    call(['python', 'tiktok.py', hashtag])
    #Load existing data to test it
    df = pd.read_csv('TikTok_data.csv')
    
    #Plotly visualization
    fig = px.histogram(df, x='desc', y='stats_diggCount', hover_data=['desc'], height=300)
    fig.update_layout(font_family="Arial", title_font_family="Arial Black", xaxis_title="Description", yaxis_title="# Likes")
    st.plotly_chart(fig, use_container_width=True)

    #Split columns
    left_col, right_col = st.columns(2)

    #First Chart - Video Stats
    scatter1 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount', title='Author Stats ⭐')
    scatter1.update_layout(font_family="Arial", title_font_family="Arial Black", xaxis_title="# Videos", yaxis_title="# Hearts")
    left_col.plotly_chart(scatter1, use_container_width=True)

    #Second Chart 
    scatter2 = px.scatter(df, x='author_verified', y='stats_diggCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='stats_playCount', title='¿Being Verified Influences? ✅')
    scatter2.update_layout(font_family="Arial", title_font_family="Arial Black", xaxis_title="Verified", yaxis_title="# Likes")
    right_col.plotly_chart(scatter2, use_container_width=True)
    
    #Third Chart 
    scatter3 = px.scatter(df, x='stats_playCount', y='stats_diggCount', hover_data=['desc'], size='stats_playCount', color='stats_commentCount', title='Video Stats 📈')
    scatter3.update_layout(font_family="Arial", title_font_family="Arial Black", xaxis_title="# Views", yaxis_title="# Likes")
    st.plotly_chart(scatter3, use_container_width=True)
    
    
    #Show tabular dataframe in Streamlit
    df
