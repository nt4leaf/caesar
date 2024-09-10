import streamlit as st

st.text("Encode:")
string_encode = st.text_input('Encode string:')
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
st.text("Encode: ")
st.write(result_encode)

st.text("Decode:")
string_decode = st.text_input('Decode string:')
data_decode = list(string_decode)
result_decode = []
for k in range(25):
  for i in range(len(data_decode)):
    if data_decode[i].isspace():
      continue
    if data_decode[i].islower():
      data_decode[i] = chr((ord(data_decode[i]) - 72) % 26 + 97)
    if data_decode[i].isupper():
      data_decode[i] = chr((ord(data_decode[i]) - 40) % 26 + 65)
  result = ''.join(data_decode)
  result_decode.append(result)
st.header("Decode")
st.write(result_decode)
