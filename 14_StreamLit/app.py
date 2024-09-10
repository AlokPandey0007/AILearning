import pandas as pd 
import streamlit as st 
import numpy as np 

st.title("This is my first app")
st.text_input("Input your name",max_chars=10)

df=pd.DataFrame({
    'first_column':[1,3,5,7,9],
    'second_column' :[2,4,6,8,0]
})

st.write("Here is dataframe")
st.write(df)