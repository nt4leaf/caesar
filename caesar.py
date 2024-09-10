import streamlit as st

my_string = st.text_input('Input string:')
step = st.number_input('Input step:')
data = list(my_string)
for i in range(len(data)):
  if data[i].isspace():
      continue
  if data[i].islower():
    data[i] = chr((ord(data[i]) + step - 97) % 26 + 97)
  if data[i].isupper():
    data[i] = chr((ord(data[i]) + step - 65) % 26 + 65)
result = ''.join(data)
st.write("Result: "result)
