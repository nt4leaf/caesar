import streamlit as st

st.text("Encode:")
string_encode = st.text_input('Input string:')
step = st.number_input('Input step:', step = 1)
data_encode = list(string_encode)
for i in range(len(data_encode)):
  if data_encode[i].isspace():
      continue
  if data_encode[i].islower():
    data_encode[i] = chr((ord(data_encode[i]) + step - 97) % 26 + 97)
  if data_encode[i].isupper():
    data_encode[i] = chr((ord(data_encode[i]) + step - 65) % 26 + 65)
result_encode = ''.join(data_encode)
st.text("Result: ")
st.write(result_encode)
