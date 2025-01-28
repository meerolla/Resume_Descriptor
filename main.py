import langchain_helper as lch
import streamlit as st

st.title("Resume description creator")


#key_words = st.text_input(label="Enter key words to generate resume descriptor")

with st.form(key='my_form'):
	key_words = st.text_area(label='Enter key words to generate resume descriptor')
	submit_button = st.form_submit_button(label='Submit')

if key_words:
    response = lch.generate_resume_descriptor(key_words)
    st.text(response)




    
