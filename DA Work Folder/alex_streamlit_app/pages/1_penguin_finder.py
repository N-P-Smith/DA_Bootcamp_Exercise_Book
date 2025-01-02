import streamlit as st
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

import time

import seaborn as sns
import matplotlib.pyplot as plt


st.title("Penguin Finder")
st.image("./data/lter_penguins.png", width=300)

col1, col2 = st.columns(2)

with col1: 
    # reading the data
    df = pd.read_csv('./data/penguins_cluster.csv')

    # selecting only nummerical columns
    df_num = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]

    # standardizing the featiures
    scaler = StandardScaler()
    scaler.fit(df_num)
    df_num_scaled = scaler.transform(df_num)

    # converting the array to a pandas dataframe with original column names
    df_penguins = pd.DataFrame(df_num_scaled, columns=df_num.columns)

    # KMeans clusterung with 3 clusters (found with elbow method)
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(df_penguins)

    st.button("Find your penguin!", type="primary")    

    bill = st.number_input("Bill Length in mm (between 32-60 mm ): ", value=df['bill_length_mm'].mean().astype(int), min_value=32, max_value=60, )
    bill_d = st.number_input("Bill Depth in mm (between 13-22 mm): ", value=df['bill_depth_mm'].mean().astype(int), min_value=13, max_value=22 )
    flipper = st.number_input("Flipper Length in mm (between 172-230 mm ): ", value=df['flipper_length_mm'].mean().astype(int), min_value=172, max_value=230)
    mass = st.number_input("Body Mass in gram (between 2700-6300 g): ", value=df['body_mass_g'].mean().astype(int), min_value=2700, max_value=6300)

    penguins = {'bill_length_mm': bill, 'bill_depth_mm': bill_d, 'flipper_length_mm': flipper, 'body_mass_g': mass}
    penguins_df = pd.DataFrame(penguins, index=['0'])

    p_scaled = scaler.transform(penguins_df)
    p_scaled_df = pd.DataFrame(p_scaled, columns = penguins_df.columns)

    cluster1 = kmeans.predict(p_scaled_df)
    cluster2 = cluster1[0]

    if cluster2 == 0 :
        penguin_text = "Your penguin is a Gentoo!"
        penguin_picture = "./data/pinguin_pic/gentoo.jpg"

    elif cluster2 == 1 :
        penguin_text = "Your penguin is a Adelie!"
        penguin_picture = "./data/pinguin_pic/adelie.jpg"
    else :
        penguin_text = "Your penguin is a Chinstrap!"
        penguin_picture = "./data/pinguin_pic/chinstrap.jpg"

with col2:
    if st.button("Show my Penguin!"):
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)

        st.snow()
        st.image(penguin_picture, caption=penguin_text, width = 300)


st.header("Are metrics of penguin species correlated?")

penguins = pd.read_csv('./data/penguins_pimped.csv')

fig, ax = plt.subplots(figsize = (10, 6))

x_vals = st.selectbox("x axis", penguins.columns[2:6])
y_vals = st.selectbox("y axis", penguins.columns[5:1:-1])

ax = sns.scatterplot(data = penguins, 
                x = x_vals, 
                y = y_vals, 
                hue = 'species', 
                style = 'sex', 
                s = 80, 
                alpha = 0.8,
                palette = 'hls')

selected_penguin = {
    'bill_length_mm': bill,
    'bill_depth_mm': bill_d,
    'flipper_length_mm': flipper,
    'body_mass_g': mass
}

# Add a black dot
ax.plot(selected_penguin[x_vals], selected_penguin[y_vals], 's', markersize=10, color='black')

# Annotate the black dot
ax.annotate('Here is your penguin!', 
            xy=(selected_penguin[x_vals], selected_penguin[y_vals]), 
            xytext=(selected_penguin[x_vals]*0.948, selected_penguin[y_vals]*1.17),
            arrowprops=dict(facecolor='black', shrink=0.2, color='black'),
            color='black')

plt.title('Yes, they are correlated')
plt.xlabel(x_vals.replace("_", " "))
plt.ylabel(y_vals.replace("_", " "))

st.pyplot(fig)