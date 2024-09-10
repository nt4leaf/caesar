import streamlit as st

st.text("Decode:")
string_decode = st.text_input('Decode string:')
data_decode = list(string_decode)
result_decode = []
#for k in range(1,25):
  for i in range(len(data_decode)):
    if data_decode[i].isspace():
        continue
    if data_decode[i].islower():
      data_decode[i] = chr((ord(data_decode[i]) + step - 72) % 26 + 97)
    if data_decode[i].isupper():
      data_decode[i] = chr((ord(data_decode[i]) + step - 40) % 26 + 65)
      data_decode = ''.join(data_decode)
  result = ''.join(data_decode)
  result_decode.append(result)
  st.text("Result: ")
  st.write(result_decode)
