import streamlit as st
import pandas as pd
from pydantic import ValidationError
import os
#import models
import sys
from models import Contact
from utils import save_to_excel


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
            phone_number = phone
        )

        save_to_excel(user)

        st.success("Submitted succesfully")
        st.write("**Submitted Data**")
        st.write(f"- Name: {user.name}")
        st.write(f"- Email: {user.email}")
        st.write(f"- Age: {user.age}")
        st.write(f"- Phone: {user.phone_number}")

    except ValidationError as e:
        st.error("Validation Error")
        for error in e.errors():
            field = error['loc'][0]
            message = error['msg']
            st.error(f"**{field}**: {message}")

    except Exception as e:
        st.error(f"Unexpected Error : {str(e)}")
