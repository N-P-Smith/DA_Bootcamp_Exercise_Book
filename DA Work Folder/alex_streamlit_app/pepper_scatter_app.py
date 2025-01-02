import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


"""### Pepper Scatters are great in figuring things out!
- look at that
- and  that 
- and this ;)
"""

df = px.data.gapminder()

country = st.multiselect("",df['country'].unique(), default=['Algeria', 'Iceland'])
country_mask = df['country'].isin(country)
df_country = df[country_mask]

# Plot 1

st.header('Life Expectancy')

fig, ax = plt.subplots(figsize = (10, 6))

ax = sns.lineplot(data=df_country, x='year', y='lifeExp', hue='country', marker='o')
plt.title(f"Live Expectancy in {country}")
plt.grid()

st.pyplot(fig)

st.header('Flying bubbles')

continent = st.radio("Select a continent", df['continent'].unique(), horizontal=True)
df2 = df[df['continent']==continent]

# Plot 2
fig2 = px.scatter(df2,
                  x='gdpPercap',
                  y='lifeExp',
                  animation_frame='year',
                  animation_group='country',
                  size='pop',
                  color='country',
                  color_discrete_sequence = px.colors.qualitative.G10,
                  log_x=True,
                  size_max=55, range_x=[100,100000], range_y=[25,90],
                  text='country',
                  title="Life Expectancy vs. GDP per Capita over Time"
                  )

# Update layout
fig2.update_layout(title_x=0.3, margin=dict(t=40))

# Update traces to align text
fig2.update_traces(textposition='top left')

st.plotly_chart(fig2)

with st.expander("See Dataframe"):
    st.dataframe(df2, width=900, hide_index=True)

st.header('Penguins Dataset')

# penguins data
penguins = sns.load_dataset('penguins')

# Add Species selection 
species = st.multiselect('Select Species', 
                         ('Adelie', 'Chinstrap', 'Gentoo'), default=penguins['species'].unique() )

# ADD COLUMNS TO organize the value-selectboxes 
# col_left, col_right = st.columns(2)

# make the choice of variable optional
# with col_left:
x_vals = st.selectbox('Select 1st Variable', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']) # penguins.columns[2:6]
# with col_right:
y_vals = st.selectbox('Select 2nd Variable', ['body_mass_g', 'flipper_length_mm', 'bill_depth_mm', 'bill_length_mm']) # penguins.columns[5:1:-1]

# subset df
df = penguins[penguins['species'].isin(species)]

fig, ax = plt.subplots(figsize = (10, 6))

ax = sns.scatterplot(data = df, 
                x = x_vals, 
                y = y_vals, 
                hue = 'species', 
                style = 'sex', 
                s = 80, 
                alpha = 0.8,
                palette = 'hls')
plt.title('Yes, they are correlated')
plt.xlabel(x_vals.replace("_", " "))
plt.ylabel(y_vals.replace("_", " "))

st.pyplot(fig)