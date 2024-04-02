# from dash import Dash, dcc, html, Input, Output, callback
#
# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# ####END
# #####
# import re
# import json
# import dash
# from dash import Dash, html, Input, Output, State, ALL, dash_table, MATCH, dcc
# import dash_bootstrap_components as dbc
# import sqlite3
# import pandas as pd
# import copy
# from dash.exceptions import PreventUpdate
# # from dash_extensions.enrich import DashProxy, html, Output, Input, dcc
# from io import BytesIO
# import base64
# import numpy as np
# from django_plotly_dash import DjangoDash
# # from DjangoDash import *
# app = DjangoDash('gesispy',external_stylesheets=[
#     dbc.themes.BOOTSTRAP])  # CYBORG COSMO select themes from: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
#
# app.layout = html.Div(
#     [
#         html.I("Try typing in input 1 & 2, and observe how debounce is impacting the callbacks. Press Enter and/or Tab key in Input 2 to cancel the delay"),
#         html.Br(),
#         dcc.Input(id="input1", type="text", placeholder="", style={'marginRight':'10px'}),
#         dcc.Input(id="input2", type="text", placeholder="", debounce=True),
#         html.Div(id="output"),
#     ]
# )
#
#
# @callback(
#     Output("output", "children"),
#     Input("input1", "value"),
#     Input("input2", "value"),
# )
# def update_output(input1, input2):
#     return f'Input 1 {input1} and Input 2 {input2}'