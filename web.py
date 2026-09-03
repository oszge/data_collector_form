import streamlit as st
import dac
from datetime import datetime, date
from pathlib import Path


def load_css(file_path: str) -> None:
    css = Path(file_path).read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css("styles.css")

FORM_DEFAULTS = {
    "first_name": "",
    "middle_name": "",
    "last_name": "",
    "date_of_birth": None,
    "gender": None,
    "phone_number": "",
    "email_address": "",
    "address_line_1": "",
    "address_line_2": "",
    "city_name": "",
    "state_province": "",
    "postal_code": "",
    "country": None,
    "highest_level_of_education": None,
    "institution": "",
    "year_of_graduation": None,
    "employment_status": None,
    "job_name": "",
    "company_name": "",
    "consent": False,
}


def reset_fields():
    for key, default_value in FORM_DEFAULTS.items():
        st.session_state[key] = default_value

    st.session_state["reset_success"] = True

st.set_page_config(
    page_title= "Data Collector Form",
    layout= "centered"
)

st.title("Personal Data Collector", text_alignment="center")


with st.container(width="stretch", border=True):
    with st.container(width="stretch", border=True): 
        st.markdown("#### **👤 Personal Details**",text_alignment="left")

        fn,mn,ln=st.columns([1,1,1])
        with fn:
            first_name=st.text_input("First Name *", placeholder="Enter first name", width="stretch", key="first_name")
            
        with mn:
            middle_name=st.text_input("Middle Name", placeholder="Enter middle name (optional)", width="stretch", key="middle_name")
        
        with ln:
            last_name=st.text_input("Last Name *", placeholder="Enter last name", width="stretch", key="last_name")

        
        dob, gndr=st.columns([1,1])
        with dob:
            today = datetime.today()

            available_years = [datetime(year, 1, 1) for year in range(1900, 2027)]
            
            date_of_birth = st.date_input("Date of Birth*", value=None, min_value=date(1900, 1, 1),max_value=date.today(), key="date_of_birth")
        
        with gndr: 
            gender = st.radio(
                "Gender *",
                ["Male", "Female", "Other"],
                horizontal=True, 
                index=None,
                key="gender")
        

        pn, ea=st.columns([1,1])
        with pn:
            phone_number=st.text_input("Phone Number *", placeholder="Enter phone number", width="stretch", key="phone_number")
            if any(character.isalpha() for character in phone_number):
                st.error("The phone number cannot contain letters.")
        
        with ea: 
            email_address=st.text_input("Email Address *", placeholder="Enter email address", width="stretch", key="email_address")

    #ADDRESS INFORMATION FIELDS

    with st.container(
        width="stretch",
        border=True,
    ):
        
        st.markdown("#### **🏠 Address Information**")

        ad1, ad2= st.columns([1, 1])

        with ad1:
            address_line_1 = st.text_input(
                "Address Line 1 *",
                placeholder= "Enter address line",
                key="address_line_1"
            )

        with ad2:
            address_line_2 = st.text_input(
                "Address Line 2",
                placeholder= "Enter address line 2 (optional)",
                key="address_line_2"
            )


        city, state = st.columns([1, 1])

        with city:
            city_name = st.text_input(
                "City *",
                placeholder= "Enter city",
                key="city_name"
            )

        with state:
            state_province = st.text_input(
                "State / Province",
                placeholder= "Enter state / province (optional)",
                key="state_province"
            )
        country, postal = st.columns([1, 1])

        with postal:
            postal_code = st.text_input(
                "Postal Code / ZIP Code *",
                placeholder= "Enter postal code",
                key="postal_code"
            )
            if any(character.isalpha() for character in postal_code):
                st.error("The postal code cannot contain letters.")

        
        with country:
            country = st.selectbox(
            "Country *",
            [
                "Hungary",
                "Germany",
                "Austria",
                "Romania",
                "Slovakia",
                "Croatia",
                "Serbia",
                "Ukraine",
                "Poland",
                "Czech Republic",
                "United Kingdom",
                "Norway",
                "Sweden",
                "Netherland",
                "Belgium",
                "Italy",
                "Spain",
                "Portugal",
                "Turkey"
            ],
            index=None,
            placeholder="Select country",
            key="country"
        )

        

    #EDUCATION FIELDS
    with st.container(
        width="stretch",
        border= True,
        
    ):
        st.markdown("#### **🎓 Education**", text_alignment="left")
        
        hle,inst,yog=st.columns([1,1,1])
        with hle:
            highest_level_of_education = st.selectbox("Highest Level of Education *",
                                                    ["High School Diploma", "Bachelor's Degree", "Master's Degree", "PHD"],
                                                    index=None, placeholder="Select education level",
                                                    key="highest_level_of_education")

        with inst:
            institution=st.text_input("Institution *", placeholder="Enter institution", key="institution")
        
        with yog:
            year_of_graduation=st.selectbox("Year Of Graduation *", list(range(1900, 2027)),index=None, placeholder="Select year", key="year_of_graduation")
        
    #EMPLOYMENT FIELDS

    with st.container(
        width="stretch",
        border=True,
    ):
        
        st.markdown("#### **💼 Employment**", text_alignment="left")

        status, job, company = st.columns([1, 1, 1])

        with status:
            employment_status = st.selectbox(
                "Current Employment Status *",
                [
                "Employed",
                "Unemployed",
                "Student",
                "Self - employed",
                "Retired"
                ],
                index=None,
                placeholder= "Select status",
                key="employment_status"
            )

        with job:
            job_name = st.text_input(
                "Current Job/Position Name",
                placeholder= "Enter job name",
                key="job_name"
            )
            if any(character.isdigit() for character in job_name):
                st.error("The job name field cannot contain numbers.")

        with company:
            company_name = st.text_input(
                "Company / Organization",
                placeholder= "Enter company name",
                key="company_name"
            )
            if any(character.isdigit() for character in company_name):
                st.error("The company name field cannot contain numbers.")

    #SUBMIT, SHOW DATA AND RESET BUTTONS
    consent = st.checkbox("I consent to data processing", key="consent")

    submit, show, reset = st.columns(3)

    #SUBMIT BUTTON-->SAVING ANSWERS INTO DATABASE
    with submit:
        submit_clicked = st.button(
            "Submit answers",
            type="primary",
            width="stretch",
            disabled=not consent
        )

    #SHOW_DATA BUTTON-->DISPLAY ANSWERS ON A NEW WEB PAGE IN TABLE FORAMT
    with show:
        show_clicked = st.button(
            "Show answers",
            type="secondary",
            width="stretch",
        )

    #RESET BUTTON-->RESETTING FIELDS SESSION STATES
    with reset:
        reset_clicked = st.button(
            "Reset answers",
            type="tertiary",
            width="stretch",
            on_click=reset_fields
        )

if submit_clicked:

    if submit_clicked:
        required_fields = {
        "First Name": first_name,
        "Last Name": last_name,
        "Date of Birth": date_of_birth,
        "Gender": gender,
        "Phone Number": phone_number,
        "Email Address": email_address,
        "Address Line 1": address_line_1,
        "City": city_name,
        "Postal Code": postal_code,
        "Country": country,
        "Education Level": highest_level_of_education,
        "Institution": institution,
        "Year of Graduation": year_of_graduation,
        "Employment Status": employment_status,
    }

    missing_fields = [
        field_name
        for field_name, value in required_fields.items()
        if value is None or (isinstance(value, str) and not value.strip())
    ]

    if missing_fields:
        st.error(
            "Please fill out the following fields: "
            + ", ".join(missing_fields)
        )

    elif any(character.isalpha() for character in phone_number):
        st.error("The phone number cannot contain letters.")

    elif any(character.isalpha() for character in postal_code):
        st.error("The postal code cannot contain letters.")

    elif any(character.isdigit() for character in job_name):
        st.error("The job name cannot contain numbers.")

    elif any(character.isdigit() for character in company_name):
        st.error("The company name cannot contain numbers.")

    elif dac.submit_answers(
        first_name,
        middle_name,
        last_name,
        date_of_birth,
        gender,
        phone_number,
        email_address,
        address_line_1,
        address_line_2,
        city_name,
        state_province,
        postal_code,
        country,
        highest_level_of_education,
        institution,
        year_of_graduation,
        employment_status,
        job_name,
        company_name
    ):
        st.success("Successfully submitted your answers!")

    else:
        st.error("Failed to submit your answers.")

if show_clicked:
    #SHOW ANSWERS
    st.switch_page("pages/display.py")

if st.session_state.pop("reset_success", False):
    st.success("Fields set back to default values", width="stretch")