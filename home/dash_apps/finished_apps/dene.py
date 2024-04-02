
import dash
from dash import clientside_callback, html, Input, Output, MATCH
import dash_bootstrap_components as dbc
import json
import time
from django_plotly_dash import DjangoDash
import dash
from dash import clientside_callback, html, Input, Output, MATCH, dcc, no_update
import dash_bootstrap_components as dbc
import json
import time
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
app = DjangoDash('profplotly',external_stylesheets=[
    dbc.themes.BOOTSTRAP])  # CYBORG COSMO select themes from: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

app.layout = html.Div(
                        [
                            dmc.LoadingOverlay(
                                html.Div(id='loading-customize-output',
                                        children=[
                                            dbc.Button(children=["Click Me!"],
                                                id="customize-button",
                                                n_clicks=0,
                                                class_name='d-grid gap-2 col-12 mx-auto btn btn-dark',
                                            ),
                                ]),
                                    loaderProps={"variant": "dots", "color": "white"},
                                    overlayColor="rgba(0, 0, 0, 0.8)",
                                    overlayBlur=10,
                                    zIndex=1000,
                            )
                        ]
                        )
@app.callback(
        Output("loading-customize-output", "children"),
        Input("customize-button", "n_clicks"),
)
def func(n_clicks):
    time.sleep(4)
    return no_update

import zipfile
from zipfile import ZipFile
import os
import shutil
import time

list=[]
a="ZA7691_v1-0-0.sav"
b="ZA7782_v1-0-0.sav"
list.append(a)
list.append(b)

def create_zip(path,list):
    zname='/home/bilgi/Downloads/Zipped_file.zip'
    for x in list:

        with ZipFile(zname,'a') as zip_object:
            # zip_object.write(x)
            zip_object.write('{}/{}'.format(path,x))
    time.sleep(30)
    if os.path.exists(zname):
        print("ZIP file created")
    else:
        print("ZIP file not created")

create_zip(path='/home/bilgi/Downloads',list=list)