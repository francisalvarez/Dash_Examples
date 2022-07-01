import pandas as pd
import numpy as np
import plotly.express as px
from plotly.offline import plot
from dash import Dash, dcc, html, Input, Output

df = px.data.medals_long()
fig = px.bar(df, x='medal', y='count', color='nation', barmode='group')
fig2 = px.bar(df, x='medal', y='count', color='nation', barmode='group')

df2 = df.copy()
avg = df.groupby('medal')['count'].sum().reset_index().assign(nation = 'Mean')
df2 = pd.concat([df2, avg], axis=0)
fig2 = px.bar(df2, x='medal', y='count', color='nation', barmode='group')
# plot(fig)


app = Dash(__name__)

app.layout = html.Div([
    html.H1("Creating a Data Viz Table with Four Quadrants",
            style={'textAlign': 'center'}),

    html.Br(),
    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(['South Korea', 'China', 'Canada'], 'South Korea')
    ]),

    # Quadrant portion
    html.Div(children=[
        html.H3("Insert Table Here"),
        html.H3("Insert Geodate Here")
    ], style={'display': 'flex', 'flex-direction': 'row', 'textAlign': 'center'}),

    # Adding text
    html.Div(children=[
        html.H5("Adding Table Here"),
        html.H5("Adding Geodate Here")
    ], style={'width': '49%', 'float': 'right', 'display': 'flex', 'flex-direction': 'row'}),

    # Actually adding a figure text
    html.Br(),
    html.Br(),
    html.Div(children=[
        dcc.Graph(
            id='bar_graph_fig',
            figure=fig
        ),

        dcc.Graph(
            id='bar_graph_fig_w_mean',
            figure=fig2
        )
    ], style={'width': '49%', 'float': 'right', 'display': 'flex', 'flex-direction': 'row'}),


    ])



if __name__ == '__main__':
    app.run_server(debug=True)





