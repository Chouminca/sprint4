
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('/Users/chouminkafertile/Downloads/vehicles_us.csv')
df=df.fillna(0)
print(df.head(15))

st.header("This is my sprint 4 project")


show_pie_chart = st.checkbox("Show Pie Chart of Conditions")

if show_pie_chart:
    fig = px.pie(df, names='condition', title='Conditions', color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig)
else:
    fig = px.bar(df, x='model_year', y='price', title='Model Year vs Price', color='condition', barmode='group')
    st.plotly_chart(fig)

fig=px.histogram(df, y='price',x='odometer', title='Prices Based Mileage', color_discrete_sequence=px.colors.qualitative.Set3)
fig.show()

fig=px.box(df, y='price',x='odometer', title='Prices Based Mileage', color_discrete_sequence=px.colors.qualitative.Set3)
fig.show()

fig=px.pie(df, names='condition',values='model_year', title='Conditions', color_discrete_sequence=px.colors.qualitative.Set3)
fig.show()