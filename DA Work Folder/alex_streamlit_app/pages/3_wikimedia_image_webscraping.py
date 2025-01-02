import streamlit as st
import urllib.request
from bs4 import BeautifulSoup

from PIL import Image

st.subheader('Silly Image Finder')

st.sidebar.markdown("### powered by")
st.sidebar.image('./data/commons-logo-en.png')


search_phrase = st.text_input("What are you looking for?").replace(" ", "+")

if search_phrase != '':
    
    with st.spinner():

        try:
            # 1. initiate the wikimedia search 
            url = f"https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search={search_phrase}"
            page_1 = urllib.request.urlopen(url)
            soup_1 = BeautifulSoup(page_1, "lxml")
            web_links = soup_1.find("a", class_="sdms-image-result sdms-image-result--portrait")

            # get url for a middle-page with the big image
            sub_url = web_links['href']

            # open middle-page and get the image url
            page_2 = urllib.request.urlopen(sub_url)
            soup_2 = BeautifulSoup(page_2, "lxml")
            image_url = soup_2.find("div", class_="fullImageLink").a['href']

            st.image(image_url, use_column_width="always", caption="Source: "+image_url)

    #         # attempt to get and add the image title:
    #         image_title = soup_2.find("span", class_="mw-page-title-main").text[:-9]
    #         st.image(image_url, caption=image_title)
        except:
            st.stop()
