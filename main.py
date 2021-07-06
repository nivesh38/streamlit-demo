import streamlit as st
import numpy as np 
import pandas as pd 

st.title('demo app')
st.write("Table demo")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df
st.write('Line chart demo')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

st.write('plot map demo')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)

st.write('Show/hide data')
if st.checkbox('show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

    chart_data

st.sidebar.selectbox('Sidebar demo select a number ',[1,2,3,4,5,])