import streamlit as st
st.caption("Written by Nguyen Tuan")
st.header("Encode:")
string_encode = ''
string_encode = st.text_input('Encode string:')
step_encode = st.number_input('Input step-encode:', step = 1, max_value = 25)
data_encode = list(string_encode)
if string_encode != '':
  for i in range(len(data_encode)):
    if data_encode[i].isspace():
        continue
    if data_encode[i].islower():
      data_encode[i] = chr((ord(data_encode[i]) + step_encode - 97) % 26 + 97)
    if data_encode[i].isupper():
      data_encode[i] = chr((ord(data_encode[i]) + step_encode - 65) % 26 + 65)
  result_encode = ''.join(data_encode)
  st.text("Result: ")
  st.write(result_encode)

st.header("Decode:")
string_decode = ''
string_decode = st.text_input('Decode string:')
step_decode = st.number_input('Input step-decode:', step = 1, max_value = 25)
data_decode = list(string_decode)
result_decode = []
if string_decode != '':
  for i in range(len(data_decode)):
    if data_decode[i].isspace():
        continue
    if data_decode[i].islower():
      data_decode[i] = chr((ord(data_decode[i]) - 97 + 26 - step_decode) % 26 + 97)
    if data_decode[i].isupper():
      data_decode[i] = chr((ord(data_decode[i]) - 65 + 26 - step_decode) % 26 + 65)
  result_decode = ''.join(data_decode)
  st.text("Result: ")
  st.write(result_decode)

