
###END
#####
import typing as t
import io
import re
import json
import dash
from dash import Dash, html, Input, Output, State, ALL, dash_table, MATCH, dcc
import dash_bootstrap_components as dbc
import sqlite3
import pandas as pd
import copy
from dash.exceptions import PreventUpdate
# from dash_extensions.enrich import DashProxy, html, Output, Input, dcc
from io import BytesIO
import base64
import numpy as np
from django_plotly_dash import DjangoDash
import os
import time
from selenium.webdriver import ChromeOptions, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import copy
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import dash_mantine_components as dmc
import os
import zipfile
from zipfile import ZipFile
# import shutil
# from dash_extensions.snippets import send_bytes
from dash_extensions import *
from dash import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ChromeOptions, Remote

# The Docker container running Selenium


app = DjangoDash('profplotly',external_stylesheets=[
    dbc.themes.BOOTSTRAP])  # CYBORG COSMO select themes from: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

app.layout = html.Div(
    [
        html.Div(
            [
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label("Gesis Search with Keywords"),
                                html.Br(),
html.Br(),
                                dcc.Input(
                                    id="fetch-input-email",
                                    type="text",
                                    placeholder="email : i.e. xyz@xyz.com",
                                   
                                ),
                                html.Br(),
html.Br(),
                                dcc.Input(
                                    id="fetch-input-password",
                                    type="text",
                                    placeholder="password : i.e. qwerty123",
                                    
                                ),
                                html.Br(),
html.Br(),
                                dcc.Input(
                                    id="fetch-input-keyword",
                                    type="text",
                                    placeholder="search key : i.e. ZA7691,ZA7782",
                                    value="ZA7782,ZA7691"
# value="ZA7691,ZA7782"
                                ),
html.Br(),
# dbc.Button('Download', color='primary', id='btn_data',outline=True),
#                                 dcc.Download(id="download-image"),
html.Br(),

################3

#bura

 #############3

                                # html.Button(
                                #     "Search", id="fetch-btn", n_clicks=0
                                # ),
                                # html.Div(id="fetch-output"),
dcc.Download(id="download-file")
                            ],
                            md=12,
                            lg=6,
                        ),
# dcc.Download(id="download-file")

                    ]
                ),
            ]
        ),
###########
 html.Div(
    [
# dbc.Button("Search & Download", id="fetch-btn", n_clicks=0),
#         dbc.Spinner(html.Div(id="loading-output")),
dmc.LoadingOverlay(
                                html.Div(id='loading-output2',
                                        children=[
                                            dbc.Button(children=["Search & Download"],
                                                id="fetch-btn",
                                                n_clicks=0,
                                                class_name='d-grid gap-2 col-12 mx-auto btn btn-dark',
                                            ),
                                ],),
                                    loaderProps={"variant": "dots", "color": "white"},
                                    overlayColor="rgba(0, 0, 0, 0.8)",
                                    overlayBlur=10,
                                    zIndex=1000,
                                    id='loading-output',
                            )
    ],

),

        ##########33


    ]
)
SELENIUM_CMD_EXECUTOR = "http://selenium:4444/wd/hub"
# SELENIUM_CMD_EXECUTOR = "http://selenium:4444/wd/hub"
# chromedriver_path="/home/bilgi/Desktop/chromedriver"
# CHROMEDRIVER_PATH="/home/bilgi/Desktop/chromedriver"
# CHROMEDRIVER_PATH ="/usr/local/bin/chromedriver"
# d_path='/home/bilgi/Downloads/'
d_path='file:///home/seluser/Downloads'
download_name = ""
file_path=""
zip_list=[]
#

# with ZipFile('E:/Zipped file.zip', 'w') as zip_object:
#    # Adding files that need to be zipped
#    zip_object.write('E:/Folder to be zipped/Greetings.txt')
#    zip_object.write('E:/Folder to be zipped/Introduction.txt')
#
# # Check to see if the zip file is created
# if os.path.exists('E:/Zipped file.zip'):
#    print("ZIP file created")
# else:
#    print("ZIP file not created")
# def create_zip(path,list):
#     zname='/home/bilgi/Downloads/Zipped_file.zip'
#     for x in list:
#         with ZipFile(zname,'a') as zip_object:
#             zip_object.write(x)
#     time.sleep(30)
#     if os.path.exists(zname):
#         print("ZIP file created")
#     else:
#         print("ZIP file not created")
def create_zip(path,list):
    # zname='/home/bilgi/Downloads/Zipped_sav_files.zip'
    zname = 'file:///home/seluser/Downloads/Zipped_sav_files.zip'
    for x in list:

        with ZipFile(zname,'a') as zip_object:
            # zip_object.write(x)
            zip_object.write('{}/{}'.format(path,x))
    time.sleep(5)
    if os.path.exists(zname):
        print("ZIP file created")
    else:
        print("ZIP file not created")

    # for x in list:
    #     dpath='{}/{}'.format(path,x)
    #     with zipfile.ZipFile('zipped_files.zip', 'w') as zipped_f:
    #         zipped_f.writestr("file_", ''.join(x))

@app.callback(
    [Output('download-file', 'data'),
     Output("loading-output", "children"),

     ],


[Input("fetch-btn", "n_clicks"),
            Input("fetch-input-email", "value"),
            Input("fetch-input-password", "value"),
            Input("fetch-input-keyword", "value"),

 ],

    prevent_initial_call=True,

# State('download-file', 'data'),
)

############___________________________________________
# @app.callback(
# Output("download_data", "data"),
#
# Input("btn_data", "n_clicks"), prevent_initial_call=True,)
# def func(n_clicks):
#     zname = '/home/bilgi/Downloads/Zipped_sav_files.zip'
#     if n_clicks>0:
#         return dcc.send_file(zname)


############___________________________________________
# @app.callback(
#     Output("download_data", "data"),
#     Input("btn_data", "n_clicks"),
#     prevent_initial_call=True,
# )
# def func(n_clicks):
#     zname = '/home/bilgi/Downloads/Zipped_sav_files.zip'
#     if n_clicks>0:
#         return dcc.send_file(zname)
#

def update_graph(n_clicks,mail,pswrd,kword):
    # zname = '/home/bilgi/Downloads/Zipped_sav_files.zip'
    zname='file:///home/seluser/Downloads/Zipped_sav_files.zip'
    global file_path
    global download_name
    global zip_list
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    run_func(mail,pswrd,kword)

    print("_____lllll____")
    print(file_path)
    # create_zip('/home/bilgi/Downloads',zip_list)
    # create_zip('file:///home/seluser/Downloads',zip_list)  #zip yüzünden iptal edildi.
    # return dict(content=response.content, filename=fn)



    time.sleep(3)
    # return dcc.send_file(path='/home/bilgi/Downloads/Zipped_sav_files.zip', filename="Zipped_sav_files.zip")
    return dcc.send_file(path='file:///home/seluser/Downloads/Zipped_sav_files.zip',filename="Zipped_sav_files.zip")


    # bytes_io = io.BytesIO()

    # with zipfile.ZipFile(bytes_io, 'w') as zipf:
    #     zipf.writestr('mydata.json', json.dumps(["mydata"]))
    # sended_bytes = dcc.send_bytes(bytes_io.getvalue(),zname)
    # return sended_bytes




############# functions#######################3
def is_file_downloaded(filename, timeout=60):
    end_time = time.time() + timeout
    while not os.path.exists(filename):
        time.sleep(1)
        if time.time() > end_time:
            print("File not found within time")
            return False

    if os.path.exists(filename):
        print("File found")
        return True
#==================================


def run_func(mailr,pswrdr,kwordr):
    global file_path
    global download_name
    global zip_list
    print(mailr)
    print(pswrdr)
    print(kwordr)
    search_list=kwordr.split(",")
    print(search_list)
    for search in search_list:
        url = "https://login.gesis.org/realms/gesis/protocol/openid-connect/auth?client_id=gesis-gws-client&redirect_uri=https%3A%2F%2Fsearch.gesis.org%2Fresearch_data%2F{}%3Flang%3Den&state=71378aec-528d-45cd-836d-fcc3d36d1ec3&response_mode=fragment&response_type=code&scope=openid&nonce=bcba6094-c4e2-4e3d-80f0-515c1f3affe6&ui_locales=en".format(
            search)
        email = '//*[@id="username"]'
        password = '//*[@id="password"]'
        login_button = '//*[@id="kc-login"]'

        # options = ChromeOptions()
        # driver = Remote(command_executor=SELENIUM_CMD_EXECUTOR, options=options)
        # driver.implicitly_wait(5)
        #

        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--disable-gpu")  # This is important for some versions of Chrome
        # chrome_options.add_argument("--remote-debugging-port=9222")  # This is recommended
        #
        # # Set path to Chrome binary
        # chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"
        #
        # # Set path to ChromeDriver
        # chrome_service = ChromeService(executable_path="/opt/chromedriver/chromedriver-linux64/chromedriver")
        #
        # # Set up driver
        # driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


        # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
        # driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
        #                           desired_capabilities=DesiredCapabilities.CHROME)

        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': '/home/seluser/Downloads'}
        chrome_options.add_experimental_option('prefs', prefs)
        #####  *************************************************
        # options = ChromeOptions()
        driver = Remote(command_executor=SELENIUM_CMD_EXECUTOR, options=chrome_options)
        ###### *************************************************
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        el = wait.until(EC.visibility_of_element_located((By.XPATH, email)))
        el.send_keys(mailr)
        el.send_keys(Keys.ENTER)
        time.sleep(1)
        el = wait.until(EC.visibility_of_element_located((By.XPATH, password)))
        el.send_keys(pswrdr)
        el.send_keys(Keys.ENTER)
        time.sleep(4)
        print("sssssssssssss")

        try:
            db_path = '//*[@id="sidebar"]/div/div[1]/a'
            chs = '//*[@id="{}_dataset_popup"]/span[2]/select/option[5]'.format(search)
            sav_path = '//*[@id="{}_dataset_popup"]/a'.format(search)
            sav_path1 = '//*[@id="{}_dataset_popup"]/a[1]'.format(search)
            el = wait.until(EC.visibility_of_element_located((By.XPATH, db_path)))
            el.send_keys(Keys.ENTER)
            time.sleep(1)
            print("database clicked")
            el = wait.until(EC.visibility_of_element_located((By.XPATH, sav_path1)))
            el.send_keys(Keys.ENTER)
            time.sleep(1)
            print("database clicked on screen")
            dropdownbox = driver.find_elements(by=By.TAG_NAME, value="Option")
            sc = 0
            while sc < len(dropdownbox):
                print(dropdownbox[sc].text)
                if dropdownbox[sc].text.strip() == "for scientific research (incl. doctorate)":
                    dropdownbox[sc].click()
                sc += 1
            time.sleep(1)
            print("dropbox")
            sav_link = ""

            for i in range(4):
                try:
                    np = "{}[{}]".format(sav_path, i + 1)
                    print(np)
                    txt = wait.until(EC.visibility_of_element_located((By.XPATH, np)))
                    print(txt.text)
                    text = txt.text.split('.')
                    if str(text[1]).startswith("sav"):
                        sav_link = np

                        download_name = txt.text.strip().split(' ')[0]
                        zip_list.append(download_name)
                    else:
                        pass
                except:
                    pass

            el = wait.until(EC.visibility_of_element_located((By.XPATH, sav_link)))
            el.send_keys(Keys.ENTER)
            ################################ indirme olayının tamamlanmasını bekleme (kontrol mekanizması)#######################################
            # driver.find_element(By.XPATH, '//button[text()="Download"]').click()
            print(sav_link)
            print("=====")
            print("sav")
            print(download_name) #'za7619_0.sav' asdfşalsd
            print(d_path)
            print("*-*-**-**-*-*- path *0******--*-*")
            time.sleep(60)
            ##################   check algorithm ###################3
            counter = 0
            # while True:
            #     if counter > 120:
            #         break
            #     print("döngüde devam ediyor.")
            #     file_path = '{}{}'.format(d_path, download_name)
            #     if is_file_downloaded(file_path, 3):
            #         print("{} completed".format(search))
            #         break
            #     else:
            #         pass
            #     counter += 1

            ###########============================================================
            # time.sleep(download_bekleme_suresi)
            print("{} completed".format(search))
        except:
            print("handle error")
        print("completed succesfully")
        driver.quit()
    # return file_path




#
#
# @app.callback(
#     [
#         Output("meta-db", "columns"),
#         Output("meta-db", "data"),
#         Output("selected-rows", "children"),
#         Output("meta-sel", "columns"),
#         Output("meta-sel", "data"),
#         Output('storage-processed-values', 'data'),
#         Output("meta-sel", "selected_rows")
#     ],
#     [
#         Input("fetch-btn", "n_clicks"),
#         Input("submit-selected-button", "n_clicks"),
#         Input("submit-button", "n_clicks"),
#     ],
#     [
#         State("fetch-input", "value"),
#         State("meta-db", "selected_rows"),
#         State("meta-sel", "selected_rows"),
#         State("meta-sel", "data"),
#         State("input-x", "value"),
#         State("input-y", "value"),
#         State("radios", "value"),
#         State("input-z", "value"),
#
#     ],
# )
#
#
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# driver = webdriver.Remote( command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
# driver.get("http://www.example.com") # ... your testing actions ... driver.quit()
