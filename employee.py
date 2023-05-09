import streamlit as st
import pandas as pd

def main():
    st.title('Streamlit Forms and salary calculator')
    menu = ["Home","About"]
    choice = st.sidebar.sidebox("Menu",menu)
    if choice == "Home":
        st.subheader("Forms Tutorial")

        with st.form(key="form1"):
            firstname = st.text_input("Firstname")
            lastname = st.text_input("Lastname")
            dob = st.date_input("Date of Birth")
            submit_button = st.form_submit_button(label="Signup")

        if submit_button:
            st.success("Hello {} you have created an account".format(firstname))
    else:
        st.subheader("About")