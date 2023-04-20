import streamlit as st
import numpy as np
import  pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    chart_data

df = pd.DataFrame({
    'firstColumn': [1, 2, 3, 4],
    'secondColumn': [10, 20, 30, 40]
})

option = st.selectbox('Which number you want to select', df['firstColumn'])