# Importing all Libraries

import dash
from dash import Dash, html, dcc 
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Getting the data and prepping

df = px.data.gapminder()
df_germany = df[df['country'] == "Germany"]
df_germany = df_germany[['year', 'lifeExp', 'pop', 'gdpPercap']]
df_countries =df[df['country'].isin(['Germany', 'Belgium', 'Denmark'])]

# Creating Visualisations

fig1 = px.bar(df_countries, 
             x='year', 
             y='lifeExp',  
             color='country',
             barmode='group',
             height=300, title = "Germany vs Denmark & Belgium")

fig1 = fig1.update_layout(
        plot_bgcolor="#222222", paper_bgcolor="#222222", font_color="white"
    )

fig2 = px.line(df_germany, 
               x='year', 
               y='lifeExp', 
               height=300, 
               title="Life Expectancy in Germany", markers=True)

fig2 = fig2.update_layout(
        plot_bgcolor="#222222", paper_bgcolor="#222222", font_color="white"
    )

fig3 = px.choropleth(df_countries, locations='iso_alpha', 
                    projection='natural earth', animation_frame="year",
                    scope='europe',   #we are adding the scope as europe
                    color='lifeExp', locationmode='ISO-3', 
                    color_continuous_scale=px.colors.sequential.ice)

fig3 = fig3.update_layout(
        plot_bgcolor="#222222", paper_bgcolor="#222222", font_color="white", geo_bgcolor="#222222"
    )

# Creating the App

app = dash.Dash(external_stylesheets = [dbc.themes.DARKLY])

app.layout = html.Div([html.H1('Gap Minder Analysis of Germany', style={'textAlign': 'center', 'color': '#636EFA'}), 
                       html.Div(html.P("Using the gapminder data we take a look at Germany's profile"), 
                                style={'marginLeft': 50, 'marginRight': 25}),
                       html.Div([html.Div('Germany', 
                                          style={'backgroundColor': '#636EFA', 'color': 'white', 
                                                 'width': '900px', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                                 #table_updated2, 
                                 dcc.Graph(figure=fig1),  
                                 dcc.Graph(figure=fig2), 
                                 dcc.Graph(figure=fig3)])
])

if __name__ == '__main__':
     app.run_server(port=8090)

