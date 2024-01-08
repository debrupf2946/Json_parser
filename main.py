import requests
import json
import pandas as pd
import streamlit as st
from helper import df

st.title("Json Parser")
p_id=st.text_input("Product ID")
pdt=df.loc[p_id]
st.subheader("Title")
st.write(pdt["title"])
st.subheader("Price")
st.write(pdt["price"],"Rupees")

