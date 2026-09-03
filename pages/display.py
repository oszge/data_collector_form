#THIS FILE IS USED FOR DISPLAYING GIVEN ANSWERS IN A TABLE FORMAT
import pandas as pd
import streamlit as st
import dac
from pathlib import Path
import web

#load styling
web.load_css("styles.css")

st.set_page_config(
    page_title="Answers",
    layout="wide"
)

st.title(
    "Your answers",
    text_alignment="center"
)

def show_answers():
    personal = dac.show_personal_details()

    df = pd.DataFrame(
        personal,
        columns=[
            "ID",
            "First Name",
            "Middle Name",
            "Last Name",
            "Date of Birth",
            "Gender",
            "Phone Number",
            "Email"
        ]
    )
    
    st.subheader("Personal Details")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    address = dac.show_address_information()


    address_df = pd.DataFrame(
        address,
        columns=[
            "Address ID",
            "Person ID",
            "Address Line 1",
            "Address Line 2",
            "City",
            "State / Province",
            "Postal Code",
            "Country"
        ]
    )

    st.subheader("Address Information")
    st.dataframe(address_df, use_container_width=True)

    st.divider()

    education = dac.show_education_information()

    education_df = pd.DataFrame(
        education,
        columns=[
            "Education ID",
            "Person ID",
            "Highest Level of Education",
            "Institution",
            "Year of Graduation"
        ]
    )

    st.subheader("Education")

    st.dataframe(
        education_df,
        use_container_width=True
    )

    st.divider()

    employment = dac.show_employment_information()

    employment_df = pd.DataFrame(
        employment,
        columns=[
            "Employment ID",
            "Person ID",
            "Employment Status",
            "Job Position",
            "Company / Organization"
        ]
    )

    st.subheader("Employment")

    st.dataframe(
        employment_df,
        use_container_width=True
    )

with st.container(width="stretch", border=True):
    show_answers()

if st.button(
    "Back to the form",
    width="content",
    type="secondary",
):
    st.switch_page("web.py")