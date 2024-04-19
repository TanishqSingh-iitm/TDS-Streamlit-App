import streamlit as st
import pandas as pd
import numpy as np

st.title('Largest of Three Numbers Steamlit App')


number1 = st.number_input('Enter First number', 1)

number2 = st.number_input('Enter Second number', 2)

number3 = st.number_input('Enter Third number', 3)

if st.button('Find Largest Among the 3 Given Numbers'):
    largest = max([number1, number2, number3])
    st.write('### The Largest Of The 3 Numbers is ', largest)


st.write("# Student Details")
st.write("* Email: 21f3001516@ds.study.iitm.ac.in")
st.write("* Name: Tanishq Singh")
st.write("* Date: 20th April 2024")