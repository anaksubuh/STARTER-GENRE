import streamlit as st
import webbrowser

st.set_page_config(
    page_title='GENRE KOTA MAGELANG',
    page_icon='logo.png',
    layout='wide',  
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': 'https://www.extremelycoolapp.com/bug',
         'About': '# This is a header. This is an *extremely* cool app!'
    }
)

url = 'https://xzld06km-8501.asse.devtunnels.ms/'
webbrowser.open_new_tab(url)