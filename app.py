import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('/Users/chouminkafertile/Downloads/vehicles_us.csv')
df=df.fillna(0)
print(df.head(15))

st.header("This is my sprint 4 project")

import streamlit as st

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

fig=px.histogram(df, y='price',x='odometer', title='Prices Based Mileage')
fig.show()

fig=px.box(df, y='price',x='odometer', title='Prices Based Mileage')
fig.show()

fig=px.pie(df, names='condition',values='model_year', title='Conditions')
fig.show()