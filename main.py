import streamlit as st

st.title("Web Scrapper")
url = st.text_input("Enter Website to scrape data")

if st.button("Scrape Website"):
    st.write("Scraping the website...")
