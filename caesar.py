import streamlit as st

data = 'Phenikaa University'
st.write('data = ', data)
for i in range(len(data)):
  data[i] +=1
st.write(data)
