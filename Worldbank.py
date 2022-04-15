import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

st.title('World Bank Data - India')
df = pd.read_csv('World_Bank_India.csv', skiprows=4)
df.set_index("Indicator Name", inplace=True)
df1 = df.loc[['Physicians (per 1,000 people)', 'Number of deaths ages 5-9 years','People using safely managed drinking water services, rural (% of rural population)'],['2010',	'2011',	'2012',	'2013',	'2014',	'2015',	'2016',	'2017',	'2018'
]]
tdf1 = df1.transpose()
st.table(tdf1)


