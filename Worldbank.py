import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

st.title('worldBankIndia')
india = pd.read_csv('World_Bank_India.csv', skiprows=4)
st.write(india)
st.write(india.index)
