import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

st.title("DC Bikes Chart")

# load data
df = pd.read_csv('data/dc_bikes.csv', parse_dates=['datetime'])

# aggregating by date max, min temperature and the total count of rented bikes
df_aggr = df.groupby(by=df['datetime'].dt.date).agg({'temp' : ['min', 'max'], 'count' : 'sum'}).reset_index()

# renaming double level columns
df_aggr.columns = ['date', 'temp_min', 'temp_max', 'rented_sum']

# adding year, month and week columns
df_aggr['date'] = pd.to_datetime(df_aggr['date'])
df_aggr['year'] = df_aggr['date'].dt.year
df_aggr['month'] = df_aggr['date'].dt.month
df_aggr['week'] = pd.to_datetime(df_aggr['date']).dt.isocalendar().week
df_aggr['week'] = df_aggr['week'].astype(int)

# adding columns for side by side layout
col1, col2 = st.columns(2)

# dynamic filter
with col1: 
    year = st.radio('Select a year', [2011,2012], horizontal = True)
with col2: 
    month = st.selectbox('Select a month', range(1,13))

# applying filter
df_aggr_filtered = df_aggr[(df_aggr['year'] == year) & (df_aggr['month'] == month)]

# plotting filtered month and year
fig, axs = plt.subplots(figsize=(10,6))

ax1 = sns.lineplot(data=df_aggr_filtered, x=df_aggr_filtered['date'].astype(str), y='temp_min')
ax2 = sns.lineplot(data=df_aggr_filtered, x=df_aggr_filtered['date'].astype(str), y='temp_max')

plt.xticks(rotation=90)

ax3 = plt.twinx()
sns.barplot(data=df_aggr_filtered, x=df_aggr_filtered['date'].astype(str), y='rented_sum', 
            ax=ax3, color='grey', width=.5, alpha=.5)

ax3.set(ylim=(0, 10_000))
plt.title(f" Min/Max Temperature vs Number of Rented Bikes in {month}/{year}")

plt.grid()
plt.tight_layout()

st.pyplot(fig)

if st.checkbox('Show Data'):
    st.dataframe(df_aggr_filtered, use_container_width=True)

if st.toggle('Show Picture?'):
    st.image('data/dog_jump.gif', caption='random picture of dogs')