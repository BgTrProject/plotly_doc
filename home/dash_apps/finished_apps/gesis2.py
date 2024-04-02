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
# app = DjangoDash('profplotly',external_stylesheets=[
#     dbc.themes.BOOTSTRAP])  # CYBORG COSMO select themes from: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
#
#
# def get_first_value(data, selected_rows):
#     for idx, row in enumerate(data):
#         if idx in selected_rows:
#             if 'value_metadata' in row:
#                 value_metadata = row['value_metadata']
#                 if value_metadata is not None:
#                     try:
#                         value_metadata_dict = eval(value_metadata)
#                         updated_metadata = {key: value.split()[0] for key, value in value_metadata_dict.items()}
#                         row['value_metadata'] = str(updated_metadata)
#                     except:
#                         pass
#     return data
#
#
# def textbox_mapping(text):
#     my_list = text.split(',')
#     mapped_dict = {}
#     for i in range(len(my_list)):
#         mapped_dict[str(float(i + 1))] = my_list[
#             i]  # Convert the key to float, then string before assigning it to the dictionary
#     return mapped_dict
#
#
# app.layout = html.Div(
#     [
#         html.H1(
#             "GET and PREPARE DATA",
#             style={"color": "blue", "fontSize": "40px"},
#         ),
#         html.H2("Get data, select from the list"),
#         dcc.Store(id='storage-processed-values'),
#         dcc.Store(id="data-store-selected"),
#         dcc.Store(id="data-store-submit"),
#
#         html.Div(
#             [
#                 html.Br(),
#                 dbc.Row(
#                     [
#                         dbc.Col(
#                             [
#                                 dbc.Label("Name of the metadata"),
#                                 html.Br(),
#                                 dcc.Input(
#                                     id="fetch-input",
#                                     type="text",
#                                     placeholder="i.e. meta2005, meta2010...",
#                                 ),
#                                 html.Button(
#                                     "Submit", id="fetch-btn", n_clicks=0
#                                 ),
#                                 html.Div(id="fetch-output"),
#                             ],
#                             md=12,
#                             lg=6,
#                         ),
#                         dbc.Col(
#                             [
#                                 dbc.Label("After selecting, submit."),
#                                 html.Br(),
#                                 html.Button(
#                                     "Submit",
#                                     id="submit-selected-button",
#                                     n_clicks=0,
#                                 ),
#                                 html.Div(id="selected-rows"),
#                             ],
#                             md=12,
#                             lg=6,
#                         ),
#
#                         dbc.Col(
#                             [
#                                 dbc.RadioItems(
#                                     id="radios",
#                                     className="btn-group",
#                                     inputClassName="btn-check",
#                                     labelClassName="btn btn-outline-primary",
#                                     labelCheckedClassName="active",
#                                     options=[
#                                         {"label": "Option 1", "value": 1},
#                                         {"label": "Option 2", "value": 2},
#                                         {"label": "Option 3", "value": 3},
#                                         {"label": "Option 4", "value": 4},
#                                         {"label": "Option 5", "value": 5},
#                                     ],
#                                     # value=1
#                                 ),
#
#                                 html.Br(),
#
#                                 # dbc.Input(id="measure-input", placeholder="Enter measure ...", type="text"),
#
#                                 dbc.Input(id="input-x", placeholder="Enter start word...", type="text",
#                                           style={"display": "none"}),
#                                 dbc.Input(id="input-y", placeholder="Enter stop word...", type="text",
#                                           style={"display": "none"}),
#                                 dbc.Input(id="input-z", placeholder="Enter start word...", type="text",
#                                           style={"display": "none"}),
#
#                                 html.Button("Submit", id="submit-button", n_clicks=0),
#
#                             ],
#                             md=12,
#                             lg=6,
#                         ),
#                     ]
#                 ),
#             ]
#         ),
#         dash_table.DataTable(
#             id="meta-db",
#             columns=[],
#             data=[],
#             editable=False,
#             row_selectable="multi",
#             selected_rows=[],
#             style_data_conditional=[
#                 {
#                     "if": {"state": "selected"},
#                     "backgroundColor": "lightblue",
#                     "border": "1px solid blue",
#                 }
#             ],
#         ),
#
#         dash_table.DataTable(
#             id="meta-sel",
#             columns=[],
#             data=[],
#             editable=False,
#             row_selectable="multi",
#             selected_rows=[],
#             style_data_conditional=[
#                 {
#                     "if": {"state": "selected"},
#                     "backgroundColor": "lightblue",
#                     "border": "1px solid blue",
#                 }
#             ],
#         ),
#
#         html.Div([html.Button("Download xlsx", id="btn_xslx"), dcc.Download(id="download_xslx")]),
#
#     ]
# )
#
#
# @app.callback(
#     Output("input-x", "style"),
#     Output("input-y", "style"),
#     Output("input-z", "style"),
#     [Input("radios", "value")]
# )
# def update_input_visibility(option):
#     if option is None:
#         return {"display": "none"}, {"display": "none"}, {"display": "none"}
#     elif option in [1, 2, 3]:
#         return {"display": "block"}, {"display": "block"}, {"display": "none"}
#     elif option == 4:
#         return {"display": "none"}, {"display": "none"}, {"display": "none"}
#     elif option == 5:
#         return {"display": "none"}, {"display": "none"}, {"display": "block"}
#     else:
#         return {"display": "block"}, {"display": "block"}, {"display": "block"}
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
# def process_table_and_selected_rows(
#         fetch_clicks, selected_btn_clicks, submit_btn_clicks, meta_name,
#         selected_rows_db, selected_rows_sel, metadata_data,
#         start_word, stop_word, radios, input_value
# ):
#     global data_df
#     global metadata_df
#     global metadata_df2
#
#     context = dash.callback_context
#     triggered_input_id = context.triggered[0]["prop_id"].split(".")[0]
#
#     if triggered_input_id == "fetch-btn":
#         if fetch_clicks:
#             conn = sqlite3.connect("database.db")
#             try:
#                 mt1 = pd.read_sql_query(f"SELECT * FROM {meta_name}", conn)
#                 conn.close()
#
#                 columns = [{"name": i, "id": i} for i in mt1.columns]
#                 data = mt1.reset_index().to_dict("records")
#
#                 return [
#                     columns,
#                     data,
#                     [],
#                     [],
#                     [],
#                     None,
#                     []
#                 ]
#
#             except Exception as e:
#                 conn.close()
#                 return [], [], html.Div(f"Error: {e}"), [], [], None, []
#
#             # conn = sqlite3.connect()
#
#     if triggered_input_id == "submit-selected-button":
#         if selected_btn_clicks:
#             if not selected_rows_db:
#                 return [], [], html.Div("No variables selected"), [], [], None, []
#             conn = sqlite3.connect('database.db')
#             try:
#                 mt1 = pd.read_sql_query(f'SELECT * FROM {meta_name}', conn)
#                 selected_vars = [mt1.iloc[i]['index'] for i in selected_rows_db]
#                 selected_table_df = "df{}".format(meta_name[-4:])
#                 data_df = pd.read_sql_query(
#                     f"SELECT {', '.join(selected_vars)} FROM {selected_table_df}",
#                     conn
#                 )
#                 metadata_df = mt1[mt1['index'].isin(selected_vars)]
#                 conn.close()
#
#                 metadata_columns = [{'name': i, 'id': i} for i in metadata_df.columns]
#
#                 metadata_data = metadata_df.reset_index().to_dict("records")
#
#                 return [
#                     [],
#                     [],
#                     html.Div([
#                         html.Div(f"Total number of variables: {len(selected_vars)}"),
#                         html.Div(f"Selected variables: {', '.join(selected_vars)}"),
#                     ]),
#                     metadata_columns,
#                     metadata_data,
#                     [],
#                     []
#                 ]
#
#             except Exception as e:
#                 conn.close()
#                 return (
#                     [], [],
#                     html.Div(f"Error: {e}"),
#                     [], [],
#                     [], []
#                 )
#
#     if triggered_input_id == "submit-button":
#         if not submit_btn_clicks or not radios:
#             raise PreventUpdate
#         # return [], [], selected_rows_sel, metadata_columns, metadata_data, None, selected_rows_sel
#         else:
#             option = int(radios)
#
#             for row in selected_rows_sel:
#                 label = metadata_data[row]['label']
#
#                 if option == 1:
#                     result = re.sub(f"{start_word}.*?{stop_word}", start_word, label)
#                 elif option == 2:
#                     result = re.sub(fr".?{re.escape(start_word)}\b.?\b{re.escape(stop_word)}\s*", '', label)
#                 elif option == 3:
#                     result = re.sub(re.escape(start_word), stop_word, label)
#                 else:
#                     result = label
#
#                 metadata_data[row]['label'] = result
#
#             for idx, row in enumerate(metadata_data):
#                 if idx in selected_rows_sel:
#                     if option == 4:
#                         metadata_data = get_first_value(metadata_data, selected_rows_sel)
#                     elif option == 5 and input_value:
#                         row['value_metadata'] = json.dumps(textbox_mapping(input_value))
#
#             metadata_data = [{k: v for k, v in row.items() if k != 'level_0'} for row in metadata_data]
#             metadata_columns = [{"name": i, "id": i} for i in metadata_data[0].keys()]
#             metadata_df2 = pd.DataFrame(metadata_data)
#
#             processed_values = []  # Replace with appropriate processed values
#
#             return [
#                 [],
#                 [],
#                 [],
#                 metadata_columns,
#                 metadata_data,
#                 processed_values,  # Replace with appropriate processed values
#                 []  # Return an empty list to reset selected rows
#             ]
#
#     return [], [], [], [], [], [], []
#
#
# # @app.callback(Output("download_xslx", "data"), [Input("btn_xslx", "n_clicks")], prevent_initial_call=True)
# # def generate_xlsx(n_nlicks):
# #     def to_xlsx(bytes_io):
# #         global data_df
# #         global metadata_df
# #         global metadata_df2
# #         xslx_writer = pd.ExcelWriter(bytes_io, engine="xlsxwriter")  # requires the xlsxwriter package
# #         data_df.to_excel(xslx_writer, index=False, sheet_name="Sheet1")
# #         metadata_df.to_excel(xslx_writer, index=False, sheet_name="Sheet2")
# #         metadata_df2.to_excel(xslx_writer, index=False, sheet_name="Sheet3")
# #         xslx_writer.close()
# #
# #     return dcc.send_bytes(to_xlsx, "some_name.xlsx")
#
# @app.callback(
#     Output("download_xslx", "data"),
#     [Input("btn_xslx", "n_clicks")],
#     [State('meta-sel', 'data')],
#     prevent_initial_call=True
# )
# def generate_xlsx(n_clicks, metadata):
#
#         metadata_df2 = pd.DataFrame.from_records(metadata)
#
#         def to_xlsx(bytes_io):
#             xslx_writer = pd.ExcelWriter(bytes_io, engine="xlsxwriter")  # requires the xlsxwriter package
#             data_df.to_excel(xslx_writer, index=False, sheet_name="Sheet1")
#             metadata_df.to_excel(xslx_writer, index=False, sheet_name="Sheet2")
#             metadata_df2.to_excel(xslx_writer, index=False, sheet_name="Sheet3")
#             xslx_writer.close()
#
#         return dcc.send_bytes(to_xlsx, "some_name.xlsx")
#
#
#
#
#
#
#
# ##################################################################33
# ######################################################################
# #
# # from django_plotly_dash import DjangoDash
# # from dash import Dash, dcc, html, Input, Output, callback
# #
# # import plotly.express as px
# #
# # import json
# # import pandas as pd
# #
# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# #
# # app = DjangoDash('profplotly', external_stylesheets=external_stylesheets)
# #
# # styles = {
# #     'pre': {
# #         'border': 'thin lightgrey solid',
# #         'overflowX': 'scroll'
# #     }
# # }
# #
# # df = pd.DataFrame({
# #     "x": [1,2,1,2],
# #     "y": [1,2,3,4],
# #     "customdata": [1,2,3,4],
# #     "fruit": ["apple", "apple", "orange", "orange"]
# # })
# #
# # fig = px.scatter(df, x="x", y="y", color="fruit", custom_data=["customdata"])
# #
# # fig.update_layout(clickmode='event+select')
# #
# # fig.update_traces(marker_size=20)
# #
# # app.layout = html.Div([
# #     dcc.Graph(
# #         id='basic-interactions',
# #         figure=fig
# #     ),
# #
# #     html.Div(className='row', children=[
# #         html.Div([
# #             dcc.Markdown("""
# #                 **Hover Data**
# #
# #                 Mouse over values in the graph.
# #             """),
# #             html.Pre(id='hover-data', style=styles['pre'])
# #         ], className='three columns'),
# #
# #         html.Div([
# #             dcc.Markdown("""
# #                 **Click Data**
# #
# #                 Click on points in the graph.
# #             """),
# #             html.Pre(id='click-data', style=styles['pre']),
# #         ], className='three columns'),
# #
# #         html.Div([
# #             dcc.Markdown("""
# #                 **Selection Data**
# #
# #                 Choose the lasso or rectangle tool in the graph's menu
# #                 bar and then select points in the graph.
# #
# #                 Note that if `layout.clickmode = 'event+select'`, selection data also
# #                 accumulates (or un-accumulates) selected data if you hold down the shift
# #                 button while clicking.
# #             """),
# #             html.Pre(id='selected-data', style=styles['pre']),
# #         ], className='three columns'),
# #
# #         html.Div([
# #             dcc.Markdown("""
# #                 **Zoom and Relayout Data**
# #
# #                 Click and drag on the graph to zoom or click on the zoom
# #                 buttons in the graph's menu bar.
# #                 Clicking on legend items will also fire
# #                 this event.
# #             """),
# #             html.Pre(id='relayout-data', style=styles['pre']),
# #         ], className='three columns')
# #     ])
# # ])
# #
# #
# # @callback(
# #     Output('hover-data', 'children'),
# #     Input('basic-interactions', 'hoverData'))
# # def display_hover_data(hoverData):
# #     return json.dumps(hoverData, indent=2)
# #
# #
# # @callback(
# #     Output('click-data', 'children'),
# #     Input('basic-interactions', 'clickData'))
# # def display_click_data(clickData):
# #     return json.dumps(clickData, indent=2)
# #
# #
# # @callback(
# #     Output('selected-data', 'children'),
# #     Input('basic-interactions', 'selectedData'))
# # def display_selected_data(selectedData):
# #     return json.dumps(selectedData, indent=2)
# #
# #
# # @callback(
# #     Output('relayout-data', 'children'),
# #     Input('basic-interactions', 'relayoutData'))
# # def display_relayout_data(relayoutData):
# #     return json.dumps(relayoutData, indent=2)