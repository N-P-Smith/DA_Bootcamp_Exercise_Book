#Import libraries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

st.title( "Our Penguins EDA")
st.header("Penguins data")

st.image('penguins.png')

## Task 1. Load the penguins data from a file to a df

df = pd.read_csv("./data/penguins_pimped.csv")

df_sample = df.sample(5)

st.markdown("Hey this is a penguins dataframe")
st.dataframe(data=df_sample)

# Determine whivh islands are present in the data

island = df.island.unique()


# Add a select box in combination with a checkbox
island = st.selectbox("Select an island", df.island.unique())
if st.checkbox("Do you want to filter the dataframe?"):
    st.dataframe(df[df["island"] == island])


# Some plotting

fig, ax = plt.subplots()

ax = sns.scatterplot(
    data = df,
    x = "bill_length_mm",
    y = "bill_depth_mm",
    hue = "sex"
)
st.pyplot(fig)

# Add a checkbox for showing the code
if st.checkbox(" Do you want to see m y code?"):

    st.markdown("""  ax = sns.scatterplot(
    data = df,
    x = "bill_length_mm",
    y = "bill_depth_mm",
    hue = "sex"
)       """)
                
fig1 = px.scatter(data_frame=df, x="bill_length_mm", 
                  y= "bill_depth_mm", color="sex",
                  animation_frame= "species")    

st.plotly_chart(fig1)    

# Plotting on map

st.map(df, latitude = 'lat', longitude = "lon" )




