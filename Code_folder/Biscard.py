#  Required Libraries

import pandas as pd

import easyocr as e

import re

import streamlit as st

from PIL import Image , ImageDraw

import numpy as np

import io

import psycopg2 as pg2

import sqlalchemy as sql

import streamlit_option_menu

import time

from streamlit_option_menu import *

from streamlit_extras import *

from streamlit_extras.keyboard_url import keyboard_to_url

from streamlit_lottie import st_lottie

from streamlit_extras.colored_header import colored_header

import json as js

import pymongo as pm

from streamlit_extras.stateful_button import button

#______________________________________________________________________________________STARTS____________________________________________________________________________________#

# Data Extraction from text using easyocr Reader Class

reader = e.Reader(['en'])

# POSTGRESQL CONNECTIVITY
praveen = pg2.connect(host='localhost', user='postgres', password='root', database='biscardx')
cursor = praveen.cursor()

# Mongo Connectivity:
# Mongo Python connectivity
praveen_1 = pm.MongoClient('mongodb://praveen:praveenroot@ac-cd7ptzz-shard-00-00.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-01.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-02.lsdge0t.mongodb.net:27017/?ssl=true&replicaSet=atlas-ac7cyd-shard-0&authSource=admin&retryWrites=true&w=majority')
db = praveen_1['BiscardX']
collection = db['Card_Data']

class Biscardx:
  def data_x_2_sql(self):

    st.set_page_config(page_title='BiscardX Project By Praveen', layout="wide")

    with st.sidebar:  # Navbar
        selected = option_menu(
            menu_title="BiscardX Project",
            options=['Intro',"Image Process", "Load to SQL",
                     'User Access', 'Feedback'],
            icons=['mic-fill', 'image-fill', 'database-fill', 'person-square', 'chat-heart-fill'],
            menu_icon='alexa',
            default_index=0,
        )
    if  selected == 'Intro':


        st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

        def lottie(filepath):
            with open(filepath, 'r') as file:
                return js.load(file)

        # Start Intro
        col1, col2 = st.columns([7, 3])
        with col1:
            col1.write("")
            col1.write("")
            col1.write("")
            col1.write("")

            st.markdown(
                "<h1 style='font-size: 50px;'><span style='color: cyan;'>Howdy ,</span> <span style='color: white;'> I am Praveen</span> </h1>",
                unsafe_allow_html=True)

            title_text = "<h1 style='color:cyan; font-size: 60px;'>A Data Science Aspirant From India</h1>"
            st.markdown(title_text, unsafe_allow_html=True)

            title_text = "<h6 style='color:white; font-size: 15px;'>I am Detective who finding hidden pattern and insights from complex data to help for data-driven decisions, hit 'P' on keyboard to know about me</h6>"
            st.markdown(title_text, unsafe_allow_html=True)

            keyboard_to_url(key="P", url="https://www.linkedin.com/in/praveen-n-2b4004223/")

        with col2:
            file = lottie("cyan_boy_lap2.json")
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=400,
                width=500,
                key=None
            )

        st.write("")
        st.write('')
        st.write("")
        st.write('')
        st.write("")
        st.write("")
        st.write('')
        st.write("")

        # ______________________________________________________________ABOUT PROJECT______________________________________________________________________________________

        title_text = "<h1 style='color:cyan; font-size: 60px;'>About  BiscardX Project</h1>"
        st.markdown(title_text, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 8, 3])
        # with col2:
        title_text = "<h1 style='color:white; font-size: 50px;'>What Has Praveen Done in this project?</h1>"
        st.markdown(title_text, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 8, 3])
        col2.write("")
        col2.write("")
        col2.write("")
        with col2:
            file = lottie('boydoubtface.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=550,
                width=700,
                key=None
            )
        #_____________________________________________________________________________________________MONEY SEE ANIMATION__________________________#
        st.write("")
        st.write("")
        st.write("")

        def lottie(animation):
            with open(animation,'r') as file:
                return js.load(file)

        col1, col2, col3 = st.columns([3, 8, 3])
        col2.write("")
        col2.write("")
        col2.write("")
        with col2:
            file = lottie('moneysee.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=600,
                width=700,
                key=None
            )

        col1, col2, col3 = st.columns([5, 8, 3])
        # with col2:
        col2.markdown( "<h1 style='font-size: 80px;'><span style='color: cyan;'>Lets</span> <span style='color: white;'>    Explore</span> </h1>",unsafe_allow_html=True)

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        # _________________________________________________________Steps 1 __________________________________________________________

        st.write("")
        st.write("")
        st.write("")

        col1, col2, col3 = st.columns([4, 20, 3])

        with col1:
            title_text = "<h1 style='color:cyan; font-size: 50px;'>Step 1 :</h1>"
            st.markdown(title_text, unsafe_allow_html=True)
        with col2:
            title_text = "<h1 style='color:white; font-size: 50px;'>Get The Bussiness Card Image From User</h1>"
            st.markdown(title_text, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 8, 3])
        col2.write("")
        col2.write("")
        col2.write("")
        with col2:
            file = lottie('image_upload.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=600,
                width=700,
                key=None
            )

        # _________________________________________________________________________________Step 2_____________________________________________________________________________________________________________________
        st.write("")
        st.write("")
        st.write("")

        col1, col2, col3 = st.columns([4, 20, 3])
        with col1:
            title_text = "<h1 style='color:cyan; font-size: 50px;'>Step 2 :</h1>"
            st.markdown(title_text, unsafe_allow_html=True)
        with col2:
            title_text = "<h1 style='color:white; font-size: 50px;'>Data Extraction And Processing </h1>"
            st.markdown(title_text, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 10, 3])
        col2.write("")
        col2.write("")
        with col2:
            file = lottie('step2_1.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=700,
                width=900,
                key=None
            )
        col3.write("")
        col3.write("")

        # _______________________________________________________________________________step 3_____________________________________________________

        st.write("")
        st.write("")
        st.write("")

        col1, col2, col3 = st.columns([4, 23, 1])
        with col1:
            title_text = "<h1 style='color:cyan; font-size: 50px;'>Step 3 :</h1>"
            st.markdown(title_text, unsafe_allow_html=True)
        with col2:
            title_text = "<h1 style='color:white; font-size: 50px;'>Load Extracted Data Into Postgres SQL Database</h1>"
            st.markdown(title_text, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 10, 3])
        col2.write("")
        col2.write("")
        with col2:
            file = lottie('db_1.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=700,
                width=700,
                key=None
            )
            # _______________________________________________________________________________step 4_____________________________________________________

        st.write("")
        st.write("")
        st.write("")

        col1, col2, col3 = st.columns([4, 20, 3])

        with col1:
            title_text = "<h1 style='color:cyan; font-size: 50px;'>Step 4 :</h1>"
            st.markdown(title_text, unsafe_allow_html=True)
        with col2:
            title_text = "<h1 style='color:white; font-size: 50px;'>Allow User To Modify Image Data</h1>"
            st.markdown(title_text, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 10, 3])
        col1.write("")
        col1.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        with col2:
            file = lottie('step4_2.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',

                height=600,
                width=700,
                key=None
            )


        # ____________________________________________________________step 5_____________________________________________________________

        st.write("")
        st.write("")
        st.write("")

        col1, col2, col3 = st.columns([4, 20, 3])

        with col1:
            title_text = "<h1 style='color:cyan; font-size: 50px;'>Step 5 :</h1>"
            st.markdown(title_text, unsafe_allow_html=True)
        with col2:
            title_text = "<h1 style='color:white; font-size: 50px;'>Praveen Here To Share His Work To You</h1>"
            st.markdown(title_text, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([3, 10, 2])

        with col2:
            file = lottie('code_explnation.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=700,
                width=1000,
                key=None
            )
        colored_header(
            label="",
            description="",
            color_name="blue-green-70"
           )

    elif selected == 'Image Process':

        st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([4.1, 8, 3])

        col2.markdown("<h1 style='font-size: 90px;'><span style='color: cyan;'>IMAGE</span> <span style='color: white;'>UPLOAD</span> </h1>",unsafe_allow_html=True)


        def lottie(animation):
            with open(animation,'r') as file:
                return js.load(file)

        col1, col2, col3 = st.columns([3.8, 8, 3])
        col2.write("")
        with col2:
            file = lottie('imagefileupload.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=500,
                width=600,
                key=None
            )

        col1, col2, col3 = st.columns([4, 8, 5])
        Input = col2.file_uploader("upload here", label_visibility="collapsed", type=["png", "jpeg", "jpg"])
        st.write("")
        # st.write('')
        st.write("")
        col1, col2, col3 = st.columns([9.5, 8, 5])
        if col2.button('Process'):

            if Input is not None:

                image = Image.open(Input)

                save_path = "P:/python-sql connectvity/Bizcardx"

                image.save('User_input.png')

                image_array = np.array(image)    # Given Image Numpy array Matrix

                st.write("")
                st.write("")
                st.write("")
                st.write("")

                col1, col2, col3 = st.columns([4, 8, 5])

                col2.markdown("<h1 style='font-size: 50px;'><span style='color: cyan;'>GIVEN</span> <span style='color: white;'>IMAGE</span> </h1>",unsafe_allow_html=True)

                with col2:
                    colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")
                    st.write("")
                    st.write("")
                    st.image(image)
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70")


                extracted_text = reader.readtext(image_array)

                final_data = [i[1] for i in extracted_text]

                x = final_data.copy()

                # Dataframe data

                data = {
                    "company_name": [],
                    "card_holder": [],
                    "designation": [],
                    "mobile_number": [],
                    "email": [],
                    "website_url": [],
                    "area": [],
                    "city": [],
                    "state": [],
                    "pincode": [],
                    'image':[]
                }


                # Get data method :

                def get_data(text):
                    for index, value in enumerate(text):

                        # Card Holder
                        if index == 0:
                            data['card_holder'].append(value)
                            if value in x:
                                x.remove(value)

                                # Designation
                        elif index == 1:
                            data['designation'].append(value)
                            if value in x:
                                x.remove(value)

                                # Mobile Number
                        elif '-' in value:
                            data['mobile_number'].append(value)
                            if value in x:
                                x.remove(value)
                            if len(data['mobile_number']) == 2:
                                data['mobile_number'] = [','.join(data['mobile_number'])]
                                if value in x:
                                    x.remove(value)

                                    #  Email
                        elif '@' in value:
                            if len(data['email']) < 1:
                                data['email'].append(value)
                                if value in x:
                                    x.remove(value)

                                    # Website URL
                        elif value.startswith('www.') or value.startswith('www') or value.startswith('wWW.') or value.startswith(
                                'wWW'):
                            data['website_url'].append(value)
                            if value in x:
                                x.remove(value)

                        elif "www " in value.lower() or "www." in value.lower():
                            data["website_url"].append(value)
                            if value in x:
                                x.remove(value)
                        elif "WWW" in value:
                            data["website_url"] = text[4] + "." + text[5]
                            if value in x:
                                x.remove(value)
                                x.remove(text[5])


                        # Area
                        elif re.findall('^[0-9].+, [a-zA-Z]+', value):
                            data["area"].append(value.split(',')[0])
                            if value in x:
                                x.remove(value)
                        elif re.findall('[0-9] [a-zA-Z]+', value):
                            data["area"].append(value)
                            if value in x:
                                x.remove(value)

                                # City Name
                        match1 = re.findall('.+St , ([a-zA-Z]+).+', value)
                        match2 = re.findall('.+St,, ([a-zA-Z]+).+', value)
                        match3 = re.findall('^[E].*', value)
                        if match1:
                            data["city"].append(match1[0])
                            if value in x:
                                x.remove(value)
                        elif match2:
                            data["city"].append(match2[0])
                            if value in x:
                                x.remove(value)
                        elif match3:
                            data["city"].append(match3[0])
                            if value in x:
                                x.remove(value)

                                # State Name
                        state_match = re.findall('[a-zA-Z]{9} +[0-9]', value)
                        if state_match:
                            data["state"].append(value[:9])
                            if value in x:
                                x.remove(value)
                        elif re.findall('^[0-9].+, ([a-zA-Z]+);', value):
                            data["state"].append(value.split()[-1])
                            if value in x:
                                x.remove(value)
                        if len(data["state"]) == 2:
                            data["state"].pop(0)
                            if value in x:
                                x.remove(value)

                                # Pincode

                        if len(value) >= 6 and value.isdigit():
                            data["pincode"].append(value)
                            if value in x:
                                x.remove(value)
                        elif re.findall('[a-zA-Z]{9} +[0-9]', value):
                            data["pincode"].append(value[10:])
                            if value in x:
                                x.remove(value)

                get_data(final_data)

                # Data image value process
                user_image_path = 'User_input.png'  # This image given by user as input

                image = Image.open('User_input.png')


                detecteded_text = reader.readtext('User_input.png')

                draw = ImageDraw.Draw(image)

                bbx = [i[0] for i in detecteded_text]

                for cor in bbx:
                    c1, c2, c3, c4 = cor
                    draw.line((*c1, *c2, *c3, *c4, *c1), fill='cyan', width=3)
                st.write("")
                st.write("")


                col1, col2, col3 = st.columns([7, 8, 5])
                with col2:
                    file = lottie('down_arrow.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )

                st.write("")
                st.write("")
                col1, col2, col3 = st.columns([4.4, 8, 3])

                col2.markdown("<h1 style='font-size: 80px;'><span style='color: cyan;'>IMAGE</span> <span style='color: white;'>PROCESS</span> </h1>",unsafe_allow_html=True)

                col1, col2, col3 = st.columns([3.7, 8, 3])
                col2.write("")

                with col2:
                    st.write("")
                    st.write("")
                    file = lottie('image process_1.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=600,
                        width=670,
                        key=None
                    )

                col1, col2, col3 = st.columns([4, 8, 5])
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")

                col2.markdown("<h1 style='font-size: 50px;'><span style='color:White;'>Text</span> <span style='color: cyan;'>Detected</span> <span style='color: white;'>On </span><span style='color: cyan;'>Image</span> </h1>",unsafe_allow_html=True)

                with col2:
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70")
                    st.write("")
                    st.write("")
                    st.image(image)
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70")



                with open(user_image_path,'rb') as file:

                    user_image_data = file.read()

                data['image'].append(user_image_data)

                # Preprocessing

                if 'St ,' in x:
                    x.remove('St ,')
                data['company_name'].append(' '.join(x))
                df = pd.DataFrame(data)
                df['state'] = df['state'].apply(
                    lambda x: x.replace(';', '') if x.endswith(';') else (x.replace(',', '') if x.endswith(',') else x))

                df['city'] = df['city'].apply(
                    lambda x: x.replace(';', '') if x.endswith(';') else (x.replace(',', '') if x.endswith(',') else x))

                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")

                col1, col2, col3 = st.columns([3, 8, 2])

                col2.markdown("<h1 style='font-size: 70px;'><span style='color:White;'>Text</span> <span style='color: cyan;'>Extracted</span> <span style='color: white;'>On </span><span style='color: cyan;'>Image</span> </h1>",unsafe_allow_html=True)

                with col2:
                    st.write("")
                    st.write("")
                    file = lottie('text_extracted.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=800,
                        key=None
                    )
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")

                col1, col2, col3 = st.columns([2.5, 8, 1])

                with col2:

                    st.markdown( "<h1 style='font-size: 70px;'><span style='color:white;'>Report</span> <span style='color: cyan;'> Gerenated  </span><span style='color:white;'>From</span> <span style='color: cyan;'>Data</span> </h1>",unsafe_allow_html=True)
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70")
                    st.markdown(f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Company Name :</span> <span style='color:white;'>{df.loc[0,'company_name']}</span> </h1>",unsafe_allow_html=True)
                    st.markdown(f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Card Holder :</span> <span style='color:white;'>{df.loc[0,'card_holder']}</span> </h1>",unsafe_allow_html=True)
                    st.markdown(f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Designation :</span> <span style='color:white;'>{df.loc[0,'designation']}</span> </h1>",unsafe_allow_html=True)
                    st.markdown(f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Mobile Number :</span> <span style='color:white;'>{df.loc[0,'mobile_number']}</span> </h1>",unsafe_allow_html=True)
                    st.markdown(f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Email :</span> <span style='color:white;'>{df.loc[0,'email']}</span> </h1>",unsafe_allow_html=True)

                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Website Url :</span> <span style='color:white;'>{df.loc[0,'website_url']}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Area :</span> <span style='color:white;'>{df.loc[0,'area']}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>City :</span> <span style='color:white;'>{df.loc[0,'city']}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>State :</span> <span style='color:white;'>{df.loc[0,'state']}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Pincode :</span> <span style='color:white;'>{df.loc[0,'pincode']}</span> </h1>",
                        unsafe_allow_html=True)
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70")

                df.to_csv('load_data.csv',index=False)



            else:
                col1, col2, col3 = st.columns([5, 8, 3])
                col2.write("")
                col2.markdown("<h1 style='font-size: 60px;'><span style='color: cyan;'>No</span> <span style='color: white;'>Image</span><span style='color: cyan;'> Found</span> </h1>", unsafe_allow_html=True)
                col1, col2, col3 = st.columns([2, 8, 3])
                with col2:
                    file = lottie('no data found.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=900,
                        key=None
                    )

    elif selected == 'Load to SQL':

           st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
           col1, col2, col3 = st.columns([3.5, 8, 3])

           col2.markdown(
               "<h1 style='font-size: 85px;'><span style='color:white;'>Data</span> <span style='color:cyan;'>Storage</span> <span style='color: white;'>Process</span> </h1>",
               unsafe_allow_html=True)

           def lottie(animation):
               with open(animation, 'r') as file:
                   return js.load(file)

           col1, col2, col3 = st.columns([4, 8, 3])
           col2.write("")
           col2.write("")
           col2.write("")
           with col2:
               file = lottie('r.json')
               st_lottie(
                   file,
                   speed=1,
                   reverse=False,
                   loop=True,
                   quality='low',
                   # renderer='svg',
                   height=500,
                   width=600,
                   key=None
               )
           col1, col2, col3 = st.columns([6, 8, 3])
           col2.write("")
           col2.write("")
           col2.write("")

           with col2:
               file = lottie('down_arrow.json')
               st_lottie(
                   file,
                   speed=1,
                   reverse=False,
                   loop=True,
                   quality='low',
                   # renderer='svg',
                   height=300,
                   width=300,
                   key=None
               )
           # col2.write("")

           col1, col2, col3 = st.columns([5, 8, 3])
           col2.markdown(
               "<h1 style='font-size: 80px;'><span style='color:white;'>Data</span> <span style='color:cyan;'>Preview</span> </h1>",
               unsafe_allow_html=True)
           col1, col2, col3 = st.columns([8, 8, 3])

           col2.write("")
           col2.write("")
           if col2.button("View Data"):
             df = pd.read_csv('load_data.csv')
             col1, col2, col3 = st.columns([3, 8, 3])
             col2.write("")
             col2.write("")
             col2.dataframe(df)

           col1, col2, col3 = st.columns([6, 8, 3])
           col2.write("")
           col2.write("")
           col2.write("")

           with col2:
               file = lottie('down_arrow.json')
               st_lottie(
                   file,
                   speed=1,
                   reverse=False,
                   loop=True,
                   quality='low',
                   height=300,
                   width=300,
                   key=None
               )

           col1, col2, col3 = st.columns([3.2, 8, 3])
           col2.write("")
           col2.markdown(
               "<h1 style='font-size: 80px;'><span style='color:white;'>Data</span> <span style='color:cyan;'>Insertion</span><span style='color:white;'> Process</span> </h1>",
               unsafe_allow_html=True)

           col1, col2, col3 = st.columns([3.5, 8, 3])
           with col2:
               col2.write("")
               col2.write("")
               col2.write("")
               file = lottie('db_2.json')
               st_lottie(
                   file,
                   speed=1,
                   reverse=False,
                   loop=True,
                   quality='low',
                   height=600,
                   width=700,
                   key=None
               )
           col1, col2, col3 = st.columns([8.5, 8, 3])
           # col2.write("")
           col2.write("")
           if col2.button('Load Data'):
               df = pd.read_csv('load_data.csv')
               query = 'insert into biscard values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
               for i in df.loc[df.index].values:
                   cursor.execute('select * from biscard')
                   card_name = [i[0] for i in cursor.fetchall()]
                   if i[0]  not  in card_name:
                       cursor.execute(query, i)
                       praveen.commit()
                       col2.write("")
                       col2.write("")
                       col2.write("")
                       col4, col1, col2, col3 = st.columns([6, 4, 3, 3])
                       col1.markdown(
                           "<h1 style='font-size: 40px;'><span style='color:white;'>Data </span><span style='color:white;'> Loaded</span><span style='color:cyan;'> Geek!!!</span></h1>",
                           unsafe_allow_html=True)

                       col4, col1, col2, col3 = st.columns([8, 5, 8, 2])
                       with col4:
                           file = lottie('star2.json')
                           st_lottie(
                               file,
                               speed=1,
                               reverse=False,
                               loop=True,
                               quality='low',
                               height=600,
                               width=700,
                               key=None
                           )

                       with col2:
                           file = lottie('star2.json')
                           st_lottie(
                               file,
                               speed=1,
                               reverse=False,
                               loop=True,
                               quality='low',
                               height=600,
                               width=700,
                               key=None
                           )

                       with col1:
                           file = lottie('stareyeblick.json')
                           st_lottie(
                               file,
                               speed=1,
                               reverse=False,
                               loop=True,
                               quality='low',
                               height=300,
                               width=400,
                               key=None
                           )
                   else:
                       col1, col2, col3 = st.columns([18, 10, 20])
                       col2.write("")
                       col2.write("")
                       col2.write("")
                       col2.success('Given Card Data Already Exists',icon='✅')

    elif selected == "User Access":
        st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 8, 1])
        col2.markdown( "<h1 style='font-size: 100px;'><span style='color:white;'>Data</span> <span style='color:cyan;'>Manipulation</span> <span style='color: white;'>Process</span> </h1>",unsafe_allow_html=True)
        def lottie(animation):
            with open(animation, 'r') as file:
                return js.load(file)

        col1, col2, col3 = st.columns([3, 8, 3])
        # col2.write("")
        col2.write("")
        # col2.write("")
        with col2:
            file = lottie('dml_1.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=700,
                width=800,
                key=None
            )
        col1, col2, col3 = st.columns([6, 8, 3])
        col2.write("")
        col2.write("")
        # col2.write("")

        with col2:
            file = lottie('down_arrow.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=300,
                width=300,
                key=None
            )


        col1, col2, col3 = st.columns([3.5, 8, 1])
        col2.markdown(
            "<h1 style='font-size: 80px;'><span style='color:white;'>Data</span> <span style='color:cyan;'>Read</span> <span style='color: white;'>Process</span> </h1>",
            unsafe_allow_html=True)

        col1, col2, col3 = st.columns([4, 8, 3])
        col2.write("")
        col2.write("")
        # col2.write("")
        with col2:
            file = lottie('read_3.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=500,
                width=700,
                key=None
            )
        col1, col2, col3 = st.columns([4, 8, 3])
        col2.write("")
        col2.write("")
        col2.write("")

        cursor.execute('select * from biscard')
        res = [i[0] for i in cursor.fetchall()]
        with col2 :
           st.markdown("<h1 style='font-size: 20px;'><span style='color:white;'>SELECT</span> <span style='color: white;'>OPTION ⬇️ </span> </h1>",unsafe_allow_html=True)
           selected_card_name = st.selectbox(' ',res)
           query_1 = f"select * from biscard where company_name = '{selected_card_name}'"
           cursor.execute(query_1)
           res_1 = [i for i in cursor.fetchall()]

        col2.write("")
        col2.write("")
        col1, col2, col3 = st.columns([4, 8, 3])
        with col2 :
            if st.button('View Data'):
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70")
                    st.markdown(
                        f"<h1 style='font-size: 40px;'> <span style='color: cyan;'>Card</span> <span style='color:white;'>Data</span><span style='color:cyan;'> :</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Company Name :</span> <span style='color:white;'>{res_1[0][0]}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Card Holder :</span> <span style='color:white;'>{res_1[0][1]}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Designation :</span> <span style='color:white;'>{res_1[0][2]}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Mobile Number :</span> <span style='color:white;'>{res_1[0][3]}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Email :</span> <span style='color:white;'>{res_1[0][4]}</span> </h1>",
                        unsafe_allow_html=True)

                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Website Url :</span> <span style='color:white;'>{res_1[0][5]}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Area :</span> <span style='color:white;'>{res_1[0][6]}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>City :</span> <span style='color:white;'>{res_1[0][7]}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>State :</span> <span style='color:white;'>{res_1[0][8]}</span> </h1>",
                        unsafe_allow_html=True)
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Pincode :</span> <span style='color:white;'>{res_1[0][9]}</span> </h1>",
                        unsafe_allow_html=True)

                    user_image_path = 'User_input.png'
                    with open(user_image_path, 'rb') as file:
                        user_image_data = file.read()


                    # Convert the image data to a PIL image
                 
                    image = Image.open(io.BytesIO(user_image_data))
                    st.markdown(
                        f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Image ⬇️ </span> </h1>",
                        unsafe_allow_html=True)
                    st.image(image)

                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70")

        col1, col2, col3 = st.columns([7, 8, 3])
        col2.write("")
        col2.write("")
        with col2:
            file = lottie('down_arrow.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=400,
                width=300,
                key=None
            )
        #____________________________________________________________
        col1, col2, col3 = st.columns([3.5, 8, 1])
        col2.markdown(
            "<h1 style='font-size: 80px;'><span style='color:white;'>Data</span> <span style='color:cyan;'>Updation</span> <span style='color: white;'>Process</span> </h1>",
            unsafe_allow_html=True)

        col1, col2, col3 = st.columns([4, 8, 3])
        col2.write("")
        col2.write("")
        with col2:
            file = lottie('update.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=600,
                width=700,
                key=None
            )
        col2.write("")
        col2.write("")
        col2.write("")
        # Select Company Name
        cursor.execute('select * from biscard')
        company = [i[0] for i in cursor.fetchall()]

        col2.markdown(
                "<h1 style='font-size: 20px;'><span style='color:white;'>CHOOSE</span> <span style='color: white;'>OPTION ⬇️ </span> </h1>",
                unsafe_allow_html=True)
        company_name = col2.selectbox('', company)
        col2.markdown(
            "<h1 style='font-size: 20px;'><span style='color:white;'>CHOOSE</span> <span style='color: white;'>FEATURE ⬇️ </span> </h1>",
            unsafe_allow_html=True)
        updattion_option = col2.selectbox('',['Company Name', 'Card Holder','Designation','Mobile Number','Email','Website Url','Area','City','State','Pincode'])
        col2.write("")
        col2.write("")
        col2.write("")

        #__________________________________________________________________________UPDATION PROCESS_______________________________#\

        if updattion_option == "Company Name":
            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:Cyan;'>Company </span><span style='color: white;'> Name </span> <span style='color: cyan;'> Updation  </span> </h1>",
                    unsafe_allow_html=True)

                cursor.execute(f"select company_name from biscard where company_name = '{company_name}'")
                res = [i[0] for i in cursor.fetchall()]
                if len(res)>0:
                        st.markdown(
                            f"<h1 style='font-size: 29px;'><span style='color:white;'>OLD NAME  </span> <span style='color: white;'>  :  </span> <span style='color: white;'> {res[0]}</span> </h1>",
                            unsafe_allow_html=True)

                        st.markdown( f"<h1 style='font-size: 29px;'><span style='color:cyan;'>NEW NAME  ⬇️</span></h1>",unsafe_allow_html=True)

                        new_name = st.text_input(' ')
                        st.markdown( f"<h1 style='font-size: 20px;'><span style='color:white;'>NEW NAME : </span><span style='color:cyan;'> {new_name}</span></h1>",unsafe_allow_html=True)

                        if st.button('Update'):
                            cursor.execute(f"update biscard set company_name = '{new_name}' where company_name = '{company_name}'")

                            praveen.commit()
                            col1, col2, col3 = st.columns([3.8, 8, 3])
                            with col2:
                                file = lottie('star_dml.json')
                                st_lottie(
                                    file,
                                    speed=1,
                                    reverse=False,
                                    loop=True,
                                    quality='low',
                                    height=100,
                                    width=200,
                                    key=None
                                )
                            col1, col2, col3 = st.columns([6, 8, 11])
                            col2.success('Data Updated Successfully ✅')
                else:
                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)

                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

        elif updattion_option == "Card Holder":

            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:Cyan;'>Card </span><span style='color: white;'> Holder </span> <span style='color: cyan;'> Updation  </span> </h1>",
                    unsafe_allow_html=True)

                cursor.execute(f"select card_holder from biscard where company_name = '{company_name}'")
                res = [i[0] for i in cursor.fetchall()]
                if len(res) > 0:
                    st.markdown(
                        f"<h1 style='font-size: 29px;'><span style='color:white;'>OLD NAME  </span> <span style='color: white;'>  :  </span> <span style='color: white;'> {res[0]}</span> </h1>",
                        unsafe_allow_html=True)

                    st.markdown( f"<h1 style='font-size: 29px;'><span style='color:cyan;'>NEW NAME  ⬇️</span></h1>",unsafe_allow_html=True)

                    new_name = st.text_input(' ')
                    st.markdown( f"<h1 style='font-size: 20px;'><span style='color:white;'>NEW NAME : </span><span style='color:cyan;'> {new_name}</span></h1>",unsafe_allow_html=True)


                    if st.button('Update'):
                        cursor.execute(f"update biscard set card_holder = '{new_name}' where company_name = '{company_name}'")

                        praveen.commit()
                        col1, col2, col3 = st.columns([3.8, 8, 3])
                        with col2:
                            file = lottie('star_dml.json')
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                height=100,
                                width=200,
                                key=None
                            )
                        col1, col2, col3 = st.columns([6, 8, 11])
                        col2.success('Data Updated Successfully ✅')
                else:

                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)

                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

        elif updattion_option == "Designation":

            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:Cyan;'>Designation </span><span style='color: white;'> Updation  </span> </h1>",
                    unsafe_allow_html=True)

                cursor.execute(f"select designation from biscard where company_name = '{company_name}'")
                res = [i[0] for i in cursor.fetchall()]
                if len(res)>0:
                    st.markdown(
                        f"<h1 style='font-size: 29px;'><span style='color:white;'>OLD NAME  </span> <span style='color: white;'>  :  </span> <span style='color: white;'> {res[0]}</span> </h1>",
                        unsafe_allow_html=True)

                    st.markdown( f"<h1 style='font-size: 29px;'><span style='color:cyan;'>NEW NAME  ⬇️</span></h1>",unsafe_allow_html=True)

                    new_name = st.text_input(' ')
                    st.markdown( f"<h1 style='font-size: 20px;'><span style='color:white;'>NEW NAME : </span><span style='color:cyan;'> {new_name}</span></h1>",unsafe_allow_html=True)


                    if st.button('Update'):

                        cursor.execute(f"update biscard set designation = '{new_name}' where company_name = '{company_name}'")

                        praveen.commit()
                        col1, col2, col3 = st.columns([3.8, 8, 3])
                        with col2:
                            file = lottie('star_dml.json')
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                height=100,
                                width=200,
                                key=None
                            )
                        col1, col2, col3 = st.columns([6, 8, 11])
                        col2.success('Data Updated Successfully ✅')
                else:
                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)

                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

        elif updattion_option == "Mobile Number":

            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:Cyan;'>Mobile Number </span><span style='color: white;'> Updation  </span> </h1>",
                    unsafe_allow_html=True)

                cursor.execute(f"select mobile_number from biscard where company_name = '{company_name}'")
                res = [i[0] for i in cursor.fetchall()]
                if len(res)>0:
                    st.markdown(
                        f"<h1 style='font-size: 29px;'><span style='color:white;'>OLD NAME  </span> <span style='color: white;'>  :  </span> <span style='color: white;'> {res[0]}</span> </h1>",
                        unsafe_allow_html=True)

                    st.markdown(f"<h1 style='font-size: 29px;'><span style='color:cyan;'>NEW NAME  ⬇️</span></h1>",
                                unsafe_allow_html=True)

                    new_name = st.text_input(' ')
                    st.markdown(
                        f"<h1 style='font-size: 20px;'><span style='color:white;'>NEW NAME : </span><span style='color:cyan;'> {new_name}</span></h1>",
                        unsafe_allow_html=True)

                    if st.button('Update'):
                        cursor.execute(
                            f"update biscard set mobile_number = '{new_name}' where company_name = '{company_name}'")

                        praveen.commit()
                        col1, col2, col3 = st.columns([3.8, 8, 3])
                        with col2:
                            file = lottie('star_dml.json')
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                height=100,
                                width=200,
                                key=None
                            )
                        col1, col2, col3 = st.columns([6, 8, 11])
                        col2.success('Data Updated Successfully ✅')
                else:
                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

        elif updattion_option == "Email":
            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:Cyan;'>Email </span><span style='color: white;'> Updation  </span> </h1>",
                    unsafe_allow_html=True)

                cursor.execute(f"select email from biscard where company_name = '{company_name}'")
                res = [i[0] for i in cursor.fetchall()]
                if len(res)>0:
                    st.markdown(
                        f"<h1 style='font-size: 29px;'><span style='color:white;'>OLD NAME  </span> <span style='color: white;'>  :  </span> <span style='color: white;'> {res[0]}</span> </h1>",
                        unsafe_allow_html=True)

                    st.markdown(f"<h1 style='font-size: 29px;'><span style='color:cyan;'>NEW NAME  ⬇️</span></h1>",
                                unsafe_allow_html=True)

                    new_name = st.text_input(' ')
                    st.markdown(
                        f"<h1 style='font-size: 20px;'><span style='color:white;'>NEW NAME : </span><span style='color:cyan;'> {new_name}</span></h1>",
                        unsafe_allow_html=True)

                    if st.button('Update'):
                        cursor.execute(
                            f"update biscard set email = '{new_name}' where company_name = '{company_name}'")

                        praveen.commit()
                        col1, col2, col3 = st.columns([3.8, 8, 3])
                        with col2:
                            file = lottie('star_dml.json')
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                height=100,
                                width=200,
                                key=None
                            )
                        col1, col2, col3 = st.columns([6, 8, 11])
                        col2.success('Data Updated Successfully ✅')

                else:
                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

        elif updattion_option == "Website Url":

            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:Cyan;'>Website URL </span><span style='color: white;'> Updation  </span> </h1>",
                    unsafe_allow_html=True)

                cursor.execute(f"select website_url from biscard where company_name = '{company_name}'")
                res = [i[0] for i in cursor.fetchall()]
                if len(res)>0:
                    st.markdown(
                        f"<h1 style='font-size: 29px;'><span style='color:white;'>OLD NAME  </span> <span style='color: white;'>  :  </span> <span style='color: white;'> {res[0]}</span> </h1>",
                        unsafe_allow_html=True)

                    st.markdown(f"<h1 style='font-size: 29px;'><span style='color:cyan;'>NEW NAME  ⬇️</span></h1>",
                                unsafe_allow_html=True)

                    new_name = st.text_input(' ')
                    st.markdown(
                        f"<h1 style='font-size: 20px;'><span style='color:white;'>NEW NAME : </span><span style='color:cyan;'> {new_name}</span></h1>",
                        unsafe_allow_html=True)

                    if st.button('Update'):
                        cursor.execute(
                            f"update biscard set website_url = '{new_name}' where company_name = '{company_name}'")

                        praveen.commit()
                        col1, col2, col3 = st.columns([3.8, 8, 3])
                        with col2:
                            file = lottie('star_dml.json')
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                height=100,
                                width=200,
                                key=None
                            )
                        col1, col2, col3 = st.columns([6, 8, 11])
                        col2.success('Data Updated Successfully ✅')
                else:
                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

        elif updattion_option == "Area":

            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:Cyan;'>Area </span><span style='color: white;'> Updation  </span> </h1>",
                    unsafe_allow_html=True)

                cursor.execute(f"select area from biscard where company_name = '{company_name}'")
                res = [i[0] for i in cursor.fetchall()]
                if len(res)>0:
                    st.markdown(
                        f"<h1 style='font-size: 29px;'><span style='color:white;'>OLD NAME  </span> <span style='color: white;'>  :  </span> <span style='color: white;'> {res[0]}</span> </h1>",
                        unsafe_allow_html=True)

                    st.markdown(f"<h1 style='font-size: 29px;'><span style='color:cyan;'>NEW NAME  ⬇️</span></h1>",
                                unsafe_allow_html=True)

                    new_name = st.text_input(' ')
                    st.markdown(
                        f"<h1 style='font-size: 20px;'><span style='color:white;'>NEW NAME : </span><span style='color:cyan;'> {new_name}</span></h1>",
                        unsafe_allow_html=True)

                    if st.button('Update'):
                        cursor.execute(
                            f"update biscard set area = '{new_name}' where company_name = '{company_name}'")

                        praveen.commit()
                        col1, col2, col3 = st.columns([3.8, 8, 3])
                        with col2:
                            file = lottie('star_dml.json')
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                height=100,
                                width=200,
                                key=None
                            )
                        col1, col2, col3 = st.columns([6, 8, 11])
                        col2.success('Data Updated Successfully ✅')
                else:
                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

        elif updattion_option == "City":

            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:Cyan;'>City </span><span style='color: white;'> Updation  </span> </h1>",
                    unsafe_allow_html=True)

                cursor.execute(f"select city from biscard where company_name = '{company_name}'")
                res = [i[0] for i in cursor.fetchall()]
                if len(res)>0:
                    st.markdown(
                        f"<h1 style='font-size: 29px;'><span style='color:white;'>OLD NAME  </span> <span style='color: white;'>  :  </span> <span style='color: white;'> {res[0]}</span> </h1>",
                        unsafe_allow_html=True)

                    st.markdown(f"<h1 style='font-size: 29px;'><span style='color:cyan;'>NEW NAME  ⬇️</span></h1>",
                                unsafe_allow_html=True)

                    new_name = st.text_input(' ')
                    st.markdown(
                        f"<h1 style='font-size: 20px;'><span style='color:white;'>NEW NAME : </span><span style='color:cyan;'> {new_name}</span></h1>",
                        unsafe_allow_html=True)

                    if st.button('Update'):
                        cursor.execute(
                            f"update biscard set city = '{new_name}' where company_name = '{company_name}'")

                        praveen.commit()
                        col1, col2, col3 = st.columns([3.8, 8, 3])
                        with col2:
                            file = lottie('star_dml.json')
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                height=100,
                                width=200,
                                key=None
                            )
                        col1, col2, col3 = st.columns([6, 8, 11])
                        col2.success('Data Updated Successfully ✅')
                else:
                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

        elif updattion_option == "State":

            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:Cyan;'>State </span><span style='color: white;'> Updation  </span> </h1>",
                    unsafe_allow_html=True)

                cursor.execute(f"select state from biscard where company_name = '{company_name}'")
                res = [i[0] for i in cursor.fetchall()]
                if len(res)>0:
                    st.markdown(
                        f"<h1 style='font-size: 29px;'><span style='color:white;'>OLD NAME  </span> <span style='color: white;'>  :  </span> <span style='color: white;'> {res[0]}</span> </h1>",
                        unsafe_allow_html=True)

                    st.markdown(f"<h1 style='font-size: 29px;'><span style='color:cyan;'>NEW NAME  ⬇️</span></h1>",
                                unsafe_allow_html=True)

                    new_name = st.text_input(' ')
                    st.markdown(
                        f"<h1 style='font-size: 20px;'><span style='color:white;'>NEW NAME : </span><span style='color:cyan;'> {new_name}</span></h1>",
                        unsafe_allow_html=True)

                    if st.button('Update'):
                        cursor.execute(
                            f"update biscard set state = '{new_name}' where company_name = '{company_name}'")

                        praveen.commit()
                        col1, col2, col3 = st.columns([3.8, 8, 3])
                        with col2:
                            file = lottie('star_dml.json')
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                height=100,
                                width=200,
                                key=None
                            )
                        col1, col2, col3 = st.columns([6, 8, 11])
                        col2.success('Data Updated Successfully ✅')
                else:
                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

        elif updattion_option == "Pincode":

            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:Cyan;'>Pincode </span><span style='color: white;'> Updation  </span> </h1>",
                    unsafe_allow_html=True)

                cursor.execute(f"select pincode from biscard where company_name = '{company_name}'")
                res = [i[0] for i in cursor.fetchall()]
                if len(res)>0:
                    st.markdown(
                        f"<h1 style='font-size: 29px;'><span style='color:white;'>OLD NAME  </span> <span style='color: white;'>  :  </span> <span style='color: white;'> {res[0]}</span> </h1>",
                        unsafe_allow_html=True)

                    st.markdown(f"<h1 style='font-size: 29px;'><span style='color:cyan;'>NEW NAME  ⬇️</span></h1>",
                                unsafe_allow_html=True)

                    new_name = st.text_input(' ')
                    st.markdown(
                        f"<h1 style='font-size: 20px;'><span style='color:white;'>NEW NAME : </span><span style='color:cyan;'> {new_name}</span></h1>",
                        unsafe_allow_html=True)

                    if st.button('Update'):
                        cursor.execute(
                            f"update biscard set pincode = '{new_name}' where company_name = '{company_name}'")

                        praveen.commit()
                        col1, col2, col3 = st.columns([3.8, 8, 3])
                        with col2:
                            file = lottie('star_dml.json')
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                height=100,
                                width=200,
                                key=None
                            )
                        col1, col2, col3 = st.columns([6, 8, 11])
                        col2.success('Data Updated Successfully ✅')
                else:
                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)

                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70")

        col1, col2, col3 = st.columns([7, 8, 3])
        col2.write("")
        col2.write("")
        with col2:
            file = lottie('down_arrow.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=400,
                width=300,
                key=None
            )
        #_____________________________________________________________________________________________________________________________________________________________________
        col1, col2, col3 = st.columns([3.5, 8, 1])
        col2.markdown(
            "<h1 style='font-size: 80px;'><span style='color:white;'>Data</span> <span style='color:cyan;'>Deletion</span> <span style='color: white;'>Process</span> </h1>",
            unsafe_allow_html=True)

        col1, col2, col3 = st.columns([5, 8, 3])
        col2.write("")
        col2.write("")
        with col2:
            file = lottie('delete_2.json')
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=650,
                width=670,
                key=None
            )
        col2.write("")
        col2.write("")


        cursor.execute('select * from biscard')
        res = [i[0] for i in cursor.fetchall()]
        col2.markdown(
            "<h1 style='font-size: 20px;'><span style='color:white;'>SELECT</span> <span style='color: white;'>BUSINESS CARD ⬇️ </span> </h1>",
            unsafe_allow_html=True)
        delete_card = col2.selectbox('  ', res)

        if len(res)>0:

            if col2.button('Drop'):
              cursor.execute(f"delete from biscard where company_name = '{delete_card}'")
              praveen.commit()

              with col2:
                  file = lottie('delete_lasst.json')
                  st_lottie(
                      file,
                      speed=1,
                      reverse=False,
                      loop=True,
                      quality='low',
                      # renderer='svg',
                      height=400,
                      width=700,
                      key=None
                  )
              col1,col2,col3,col4 = st.columns([10,12,1,4])
              col2.markdown(
                  "<h1 style='font-size: 40px;'><span style='color:white;'>Data </span><span style='color:white;'> Deleted Successfully </span><span style='color:cyan;'> Geek!!!</span></h1>",
                  unsafe_allow_html=True)

        else:
                col1, col2, col3 = st.columns([5, 8, 3])
                with col2:
                    file = lottie('no_data.json')
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=400,
                        width=700,
                        key=None)

    elif selected == 'Feedback':
        # Mongo Python connectivity
        praveen_1 = pm.MongoClient( 'mongodb://praveen:praveenroot@ac-cd7ptzz-shard-00-00.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-01.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-02.lsdge0t.mongodb.net:27017/?ssl=true&replicaSet=atlas-ac7cyd-shard-0&authSource=admin&retryWrites=true&w=majority')
        db = praveen_1['Feedback_biscard']
        collection = db['comment']

        st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

        col1, col2, col3, = st.columns([3, 8, 3])

        with col2:
            selected_1 = option_menu(
                menu_title="OPINION BOX",
                options=['CHOOSE OPTION', 'Your Feedback', "Explore User Thoughts"],
                icons=['arrow-down-circle-fill', 'envelope-plus-fill', 'people-fill'],
                default_index=0)
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")


        if selected_1 == 'CHOOSE OPTION':
            # animation

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            col1, col2, col3 ,col4= st.columns([15, 15, 15,15])
            with col2:
                file = lottie("angry_emoji.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=300,
                    width=300,
                    key=None
                )
            with col1:
                file = lottie("smile_emoji.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=300,
                    width=300,
                    key=None
                )
            with col3:
                file = lottie("calm_emoji.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=300,
                    width=300,
                    key=None
                )
            with col4:
                file = lottie("love_emoji.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=300,
                    width=300,
                    key=None
                )


        elif selected_1 == 'Your Feedback':

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            col1, col2, col3 = st.columns([10, 30, 5])
            col2.markdown(
                "<h1 style='font-size: 90px;'><span style='color:white;'>Your</span> <span style='color:cyan;'>Feedback</span> <span style='color: white;'>Here </span> </h1>",
                unsafe_allow_html=True)
            # animation

            st.write("")

            st.write("")

            st.write("")
            col1, col2, col3 = st.columns([15, 30, 5])
            with col2 :
                file = lottie("star_before_fb.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=600,
                    key=None
                )

            col1, col2, col3, = st.columns([3, 8, 3])

            with col2:
                col2.markdown(
                    "<h1 style='font-size: 30px;'><span style='color:white;'>Enter</span> <span style='color:cyan;'>Comment</span> <span style='color: white;'>Here ⬇️</span> </h1>",
                    unsafe_allow_html=True)
                Comment = st.text_input('   ')
                st.write(Comment)
                if st.button('Save Comment'):
                    collection.insert_one({'comment of user': Comment})
                    st.write("")
                    st.write("")
                    col1, col2, col3, = st.columns([5, 8, 5])
                    st.success('Your Valuable Comment Saved Thankyou!', icon="✅")
                    col1, col2, col3 = st.columns([10, 30, 10])
                    with col2:
                        file = lottie("star.json")
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            # renderer='svg',
                            height=100,
                            width=500,
                            key=None
                        )

            col1, col2, col3, = st.columns([3, 8, 3])
            with col2 :
                colored_header(
                label="",
                description="",
                color_name="blue-green-70", )


        elif selected_1 == 'Explore User Thoughts':

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            col1, col2, col3 = st.columns([10, 30, 5])

            with col2:

                file = lottie("down_arrow.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=300,
                    width=800,
                    key=None
                )
            col2.markdown(
                "<h1 style='font-size: 70px;'><span style='color:white;'>Explore</span> <span style='color:cyan;'>User Thoughts </span> <span style='color: white;'>Here </span> </h1>",
                unsafe_allow_html=True)
            col2.write("")
            col2.write("")

            with col2:

                file = lottie("thoughts.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=800,
                    key=None
                )
            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3, = st.columns([3.6, 10, 3])
            with col2:
                # if st.button("Click Me!"):
                    res = [i['comment of user'] for i in collection.find()]
                    st.write("")
                    with st.spinner('Wait for it...'):
                        time.sleep(5)

                    colored_header(
                        label="Comments By Users ⬇",
                        description="",
                        color_name="blue-green-70", )
                    for i in res:
                        print(st.code(i))

                    col1, col2, col3 = st.columns([1, 10, 1])
                    col2.write("")
                    col2.write('')
                    col2.markdown(
                        "<h1 style='font-size: 35px;'><span style='color:cyan;'>Press</span> <span style='color:white;'>'G'</span> <span style='color:cyan;'>On Keyboard To Explore More Project</span> </h1>",unsafe_allow_html=True)
                    with col2:
                        keyboard_to_url(key="G", url="https://github.com/praveendecode")

                    def lottie(filepath):
                        with open(filepath, 'r') as file: #'G' On Keyboard To Explore More Project
                            return js.load(file)

                    with col2:
                        file = lottie("click2.json")
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=100,
                            width=700,
                            key=None
                        )



                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )



# Object creation for class Biscradx

Object = Biscardx()

Object.data_x_2_sql()

#___________________________________________________________________________FINISHED__________________________________________#
