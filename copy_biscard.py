#  Required Libraries

import pandas as pd

import easyocr as e

import re

import streamlit as st

from PIL import Image, ImageDraw

import numpy as np

import io

import psycopg2 as pg2

import sqlalchemy as sql

import streamlit_option_menu

from streamlit_option_menu import *

from streamlit_extras import *

from streamlit_extras.keyboard_url import keyboard_to_url

from streamlit_lottie import st_lottie

from streamlit_extras.colored_header import colored_header

import json as js
from streamlit_extras.stateful_button import button

# ______________________________________________________________________________________STARTS____________________________________________________________________________________#

# Data Extraction from text using easyocr Reader Class

reader = e.Reader(['en'])

# POSTGRESQL CONNECTIVITY
praveen = pg2.connect(host='localhost', user='postgres', password='root', database='biscardx')
cursor = praveen.cursor()


class Biscardx:
    def data_x_2_sql(self):

        st.set_page_config(page_title='BiscardX Project By Praveen', layout="wide")

        with st.sidebar:  # Navbar
            selected = option_menu(
                menu_title="BiscardX Project",
                options=['Intro', "Image Process", "Load to SQL",
                         'User Access', 'Feedback'],
                icons=['mic-fill', 'cash-stack', 'phone-flip', 'geo-alt-fill', 'clock-fill'],
                menu_icon='alexa',
                default_index=0,
            )
        if selected == 'Intro':

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

                title_text = "<h1 style='color: #FFFFFF; font-size: 50px;'>Howdy, I am Praveen</h1>"
                st.markdown(title_text, unsafe_allow_html=True)

                title_text = "<h1 style='color:#7FEFEA; font-size: 60px;'>A Data Science Aspirant From India</h1>"
                st.markdown(title_text, unsafe_allow_html=True)

                title_text = "<h6 style='color: #FFFFFF; font-size: 15px;'>I am Detective who finding hidden pattern and insights from complex data to help for data-driven decisions, hit 'P' on keyboard to know about me</h6>"
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
            # colored_header(
            #     label="",
            #     description="",
            #     color_name="blue-green-70"
            # )
            st.write("")
            st.write('')
            st.write("")
            st.write('')
            st.write("")
            st.write("")
            st.write('')
            st.write("")

            # ______________________________________________________________ABOUT PROJECT______________________________________________________________________________________

            title_text = "<h1 style='color:#7FEFEA; font-size: 60px;'>About  BiscardX Project</h1>"
            st.markdown(title_text, unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 8, 3])
            # with col2:
            title_text = "<h1 style='color:#FFFFFF; font-size: 50px;'>What Has Praveen Done in this project?</h1>"
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
                    height=400,
                    width=500,
                    key=None
                )
            # _____________________________________________________________________________________________MONEY SEE ANIMATION__________________________#
            st.write("")
            st.write("")
            st.write("")

            def lottie(animation):
                with open(animation, 'r') as file:
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
                    height=500,
                    width=500,
                    key=None
                )

            col1, col2, col3 = st.columns([3.8, 8, 3])
            # with col2:
            col2.markdown(
                "<h1 style='font-size: 80px;'><span style='color: cyan;'>Lets</span> <span style='color: white;'>    Explore</span> </h1>",
                unsafe_allow_html=True)

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
                title_text = "<h1 style='color:#7FEFEA; font-size: 50px;'>Step 1 :</h1>"
                st.markdown(title_text, unsafe_allow_html=True)
            with col2:
                title_text = "<h1 style='color:#FFFFFF; font-size: 50px;'>Get The Bussiness Card Image From User</h1>"
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
                    height=500,
                    width=700,
                    key=None
                )

            # _________________________________________________________________________________Step 2_____________________________________________________________________________________________________________________
            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([4, 20, 3])
            with col1:
                title_text = "<h1 style='color:#7FEFEA; font-size: 50px;'>Step 2 :</h1>"
                st.markdown(title_text, unsafe_allow_html=True)
            with col2:
                title_text = "<h1 style='color:#FFFFFF; font-size: 50px;'>Data Extraction And Processing </h1>"
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
                    height=600,
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
                title_text = "<h1 style='color:#7FEFEA; font-size: 50px;'>Step 3 :</h1>"
                st.markdown(title_text, unsafe_allow_html=True)
            with col2:
                title_text = "<h1 style='color:#FFFFFF; font-size: 50px;'>Load Extracted Data Into Postgres SQL Database</h1>"
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
                    height=600,
                    width=700,
                    key=None
                )
                # _______________________________________________________________________________step 4_____________________________________________________

            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([4, 20, 3])

            with col1:
                title_text = "<h1 style='color:#7FEFEA; font-size: 50px;'>Step 4 :</h1>"
                st.markdown(title_text, unsafe_allow_html=True)
            with col2:
                title_text = "<h1 style='color:#FFFFFF; font-size: 50px;'>Allow User To Modify Image Data</h1>"
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

                    height=500,
                    width=600,
                    key=None
                )

            # ____________________________________________________________step 5_____________________________________________________________

            st.write("")
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns([4, 20, 3])

            with col1:
                title_text = "<h1 style='color:#7FEFEA; font-size: 50px;'>Step 5 :</h1>"
                st.markdown(title_text, unsafe_allow_html=True)
            with col2:
                title_text = "<h1 style='color:#FFFFFF; font-size: 50px;'>Praveen Here To Share His Work To You</h1>"
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
                    height=600,
                    width=800,
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

            col2.markdown(
                "<h1 style='font-size: 80px;'><span style='color: cyan;'>IMAGE</span> <span style='color: white;'>UPLOAD</span> </h1>",
                unsafe_allow_html=True)

            def lottie(animation):
                with open(animation, 'r') as file:
                    return js.load(file)

            col1, col2, col3 = st.columns([3.5, 8, 3])
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

                    image_array = np.array(image)  # Given Image Numpy array Matrix

                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("")

                    col1, col2, col3 = st.columns([4, 8, 5])

                    col2.markdown(
                        "<h1 style='font-size: 50px;'><span style='color: cyan;'>GIVEN</span> <span style='color: white;'>IMAGE</span> </h1>",
                        unsafe_allow_html=True)

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
                        'image': []
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
                            elif value.startswith('www.') or value.startswith('www') or value.startswith(
                                    'wWW.') or value.startswith(
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
                    col1, col2, col3 = st.columns([3.8, 8, 3])

                    col2.markdown(
                        "<h1 style='font-size: 80px;'><span style='color: cyan;'>IMAGE</span> <span style='color: white;'>PROCESS</span> </h1>",
                        unsafe_allow_html=True)

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
                            height=500,
                            width=600,
                            key=None
                        )

                    col1, col2, col3 = st.columns([4, 8, 5])
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")

                    col2.markdown(
                        "<h1 style='font-size: 50px;'><span style='color:White;'>Text</span> <span style='color: cyan;'>Detected</span> <span style='color: white;'>On </span><span style='color: cyan;'>Image</span> </h1>",
                        unsafe_allow_html=True)

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

                    with open(user_image_path, 'rb') as file:

                        user_image_data = file.read()

                    data['image'].append(user_image_data)

                    # Preprocessing

                    if 'St ,' in x:
                        x.remove('St ,')
                    data['company_name'].append(' '.join(x))
                    df = pd.DataFrame(data)
                    df['state'] = df['state'].apply(
                        lambda x: x.replace(';', '') if x.endswith(';') else (
                            x.replace(',', '') if x.endswith(',') else x))

                    df['city'] = df['city'].apply(
                        lambda x: x.replace(';', '') if x.endswith(';') else (
                            x.replace(',', '') if x.endswith(',') else x))

                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")

                    col1, col2, col3 = st.columns([2.5, 8, 2])

                    col2.markdown(
                        "<h1 style='font-size: 70px;'><span style='color:White;'>Text</span> <span style='color: cyan;'>Extracted</span> <span style='color: white;'>On </span><span style='color: cyan;'>Image</span> </h1>",
                        unsafe_allow_html=True)

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

                        st.markdown(
                            "<h1 style='font-size: 70px;'><span style='color:white;'>Report</span> <span style='color: cyan;'> Gerenated  </span><span style='color:white;'>From</span> <span style='color: cyan;'>Data</span> </h1>",
                            unsafe_allow_html=True)
                        colored_header(
                            label="",
                            description="",
                            color_name="blue-green-70")
                        st.markdown(
                            f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Company Name :</span> <span style='color:white;'>{df.loc[0, 'company_name']}</span> </h1>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Card Holder :</span> <span style='color:white;'>{df.loc[0, 'card_holder']}</span> </h1>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Designation :</span> <span style='color:white;'>{df.loc[0, 'designation']}</span> </h1>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Mobile Number :</span> <span style='color:white;'>{df.loc[0, 'mobile_number']}</span> </h1>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Email :</span> <span style='color:white;'>{df.loc[0, 'email']}</span> </h1>",
                            unsafe_allow_html=True)

                        st.markdown(
                            f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Website Url :</span> <span style='color:white;'>{df.loc[0, 'website_url']}</span> </h1>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Area :</span> <span style='color:white;'>{df.loc[0, 'area']}</span> </h1>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>City :</span> <span style='color:white;'>{df.loc[0, 'city']}</span> </h1>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>State :</span> <span style='color:white;'>{df.loc[0, 'state']}</span> </h1>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"<h1 style='font-size: 30px;'> <span style='color: cyan;'>Pincode :</span> <span style='color:white;'>{df.loc[0, 'pincode']}</span> </h1>",
                            unsafe_allow_html=True)
                        colored_header(
                            label="",
                            description="",
                            color_name="blue-green-70")

                    # colored_header(
                    #     label="",
                    #     description="",
                    #     color_name="blue-green-70")

                    df.to_csv('load_data.csv', index=False)



                else:
                    col1, col2, col3 = st.columns([5, 8, 3])
                    col2.write("")
                    col2.markdown(
                        "<h1 style='font-size: 60px;'><span style='color: cyan;'>No</span> <span style='color: white;'>Image</span><span style='color: cyan;'> Found</span> </h1>",
                        unsafe_allow_html=True)
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
            df = pd.read_csv('load_data.csv')


        elif selected == "User Access":
            # image_data = df['image_data'][0]
            #
            # # Convert the image data to a PIL image
            # image = Image.open(io.BytesIO(image_data))
            pass


# Object creation for class Biscradx

Object = Biscardx()

Object.data_x_2_sql()