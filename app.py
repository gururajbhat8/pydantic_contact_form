import streamlit as st
import pandas as pd
from pydantic import ValidationError
import os
#import models
import sys
from models import Contact

st.title("Contact Form Validator")
with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", step=1)
    phone = st.text_input("Phone_number")

    submitted = st.form_submit_button("Submit")

if submitted:
    try:
        user = Contact(
            name = name,
            email = email,
            age = age,
            phone = phone
        )

        st.success("Submitted succesfully")

    except ValidationError as e:
        st.error(e)