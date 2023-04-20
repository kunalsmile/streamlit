import streamlit as st
import pandas as pd
import numpy as np

# Line Chart
chart_data = pd.DataFrame(np.random.randn(20, 4),
                          columns=['a', 'b', 'c', 'd'])
st.line_chart(chart_data)

# Table
df = pd.DataFrame({
    'firstColumn': [1, 2, 3, 4, 5],
    'secondColumn': [10, 20, 30, 40, 50]
})
df

# Plot Map

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# widget
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
