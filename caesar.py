import streamlit as st

my_string = st.text_input('Input string:')
step = 1
data = list(my_string)
for i in range(len(data)):
  if data[i].isspace():
      continue
  if data[i].islower():
    data[i] = chr((ord(data[i]) - 97) % 26 + step + 97)
  if data[i].isupper():
    data[i] = chr((ord(data[i]) - 65) % 26 + step + 65)
result = ''.join(data)
st.write(result)
