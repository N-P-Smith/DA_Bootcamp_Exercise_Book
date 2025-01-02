import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Our Penguins EDA")
st.header("Penguins Data")

st.image("penguins.png")

# Load data from a file to a df.

df = pd.read_csv("./data/penguins_pimped.csv")

df_sample = df.sample(5)

st.markdown("Hey, this is a Penguins Dataframe.")
st.dataframe(data = df_sample)

# Determine which islands are in the data.

island = df.island.unique()

# Add a select box in conbination with a checkbox.

island = st.selectbox("Select an island", df.island.unique())
if st.checkbox("Do you want to filter the Dataframe?"):
    st.dataframe(df[df["island"] == island])

# Some plotting.

fig, ax = plt.subplots()

ax = sns.scatterplot(
    data = df,
    x = "bill_length_mm",
    y = "bill_depth_mm",
    hue = "sex"
)

st.pyplot(fig)

# Add a checkbox for showing code.

if st.checkbox("Do you want to see the code?"):
    st.markdown("""ax = sns.scatterplot(
        data = df,
        x = "bill_length_mm",
        y = "bill_depth_mm",
        hue = "sex"
    )""")

fig1 = px.scatter(data_frame = df,
                 x = "bill_length_mm",
                 y = "bill_depth_mm",
                 color = "sex",
                 animation_frame = "species")

st.plotly_chart(fig1)

# Plotting on map.

st.map(df, lattitude = "lat", longitude = "lon")