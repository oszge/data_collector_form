import streamlit as st
import psycopg2

def connect():
    connection = None
    try:
        connection = psycopg2.connect(st.secrets["DATABASE_URL"], connect_timeout=10)
    except psycopg2.Error as e:
        st.error(f"Error connecting to the database: {e}")
        print(f"Error connecting to the database: {e}")
        return None

    return connection

def is_missing(value):
    return value is None or (isinstance(value, str) and not value.strip())

def submit_answers(fn, mn, ln, dob, gndr, phnum, eml_adrs,
                 ad_ln1, ad_ln2, city,state,p_code,cntry,
                 hl_edu, inst, yog,
                 c_emp_st, job_p, comp_org
):
    required_values = [fn,ln,dob, gndr, phnum, eml_adrs,
                 ad_ln1,city,p_code,cntry,
                 hl_edu, inst, yog,
                 c_emp_st]
    
    if any(is_missing(value) for value in required_values):
        return False

    connection = connect()

    if connection is None:
        return False
    
    try:
        with connection:
            with connection.cursor() as cursor:

                cursor.execute('''
                       INSERT INTO personal_details
                       (first_name, middle_name, last_name, date_of_birth, gender, phone_number, email_address) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING person_id;''' ,
                       [fn, mn, ln, dob, gndr, phnum, eml_adrs])
                
                person_id = cursor.fetchone()[0]

                cursor.execute('''
                        INSERT INTO address_information
                        (adrs_person_id, address_line_1, address_line_2, city, state_province, postal_code_zip_code, country)
                        VALUES (%s, %s,%s,%s,%s,%s,%s);''', 
                        [person_id, ad_ln1, ad_ln2, city, state,p_code, cntry])
                
                cursor.execute('''
                        INSERT INTO education 
                        (edu_person_id, highest_level_of_education, institution, year_of_graduation)
                        VALUES (%s, %s, %s, %s)''', 
                        [person_id, hl_edu, inst, yog])
                
                cursor.execute('''
                        INSERT INTO employment
                        (emp_person_id, current_employment_status, job_position, company_org)
                        VALUES (%s, %s, %s, %s)''', 
                        [person_id, c_emp_st, job_p, comp_org])

        return True
    except psycopg2.Error as error:
        st.error(f"Database error: {error}")
        print("Database error:", error)
        return False
    finally:
        connection.close()


def show_personal_details():
    connection = connect()
    result = None

    if connection is not None:
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM personal_details
                    ORDER BY person_id;
                    """
                )
                result = cursor.fetchall()

        except psycopg2.Error as error:
            print("Database error:", error)
            result = []

        finally:
            connection.close()
        return result

def show_address_information():
    connection = connect()
    result = None

    if connection is not None:
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM address_information
                    ORDER BY adrs_person_id;
                    """
                )
                result = cursor.fetchall()

        except psycopg2.Error as error:
            print("Database error:", error)
            result = []

        finally:
            connection.close()
        return result

def show_education_information():
    connection = connect()
    result = None

    if connection is not None:
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM education
                    ORDER BY edu_person_id;
                    """
                )
                result = cursor.fetchall()

        except psycopg2.Error as error:
            print("Database error:", error)
            result = []

        finally:
            connection.close()
        return result

def show_employment_information():
    connection = connect()
    result = None

    if connection is not None:
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM employment
                    ORDER BY emp_person_id;
                    """
                )
                result = cursor.fetchall()

        except psycopg2.Error as error:
            print("Database error:", error)
            result = []

        finally:
            connection.close()
        return result