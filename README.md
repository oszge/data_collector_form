# Personal Data Collector

Personal Data Collector is a Streamlit web application for collecting and viewing personal information. It provides a structured form for personal details, address, education, and employment data. After the user gives consent, the submission is validated and stored in a PostgreSQL database. A separate page displays the saved records in tables.

## Features

- Collects required and optional personal, address, education, and employment details.
- Validates required fields and checks phone numbers, postal codes, job titles, and company names.
- Enables submission only after the consent checkbox is selected.
- Displays saved records on a separate answers page.
- Uses a relational database with foreign keys and cascading deletes.

## Technology

- Python
- Streamlit
- PostgreSQL
- NeonDB (hosted PostgreSQL)
- `psycopg2` for database access
- pandas for displaying query results

## Project Structure

```text
.
├── dac.py                 # Database access and insert/query functions
├── db.sql                 # PostgreSQL table definitions and maintenance queries
├── requirements.txt       # Python dependencies
├── styles.css             # Streamlit application styling
├── web.py                 # Main form and application entry point
└── pages/
    └── display.py         # Page for viewing saved answers
```

## Access the Form

The application is hosted online, so no local installation or setup is required. Open the deployed application using the link provided by the project owner, complete the form, select the consent checkbox, and choose **Submit answers**. Use **Show answers** to view the stored records.

## Database

The deployed application uses NeonDB as its hosted PostgreSQL database. The database connection and schema are configured for the application, so users do not need to create a Neon project, configure credentials, or initialize the tables.

The data is organized across four related tables: `personal_details`, `address_information`, `education`, and `employment`. Related records use foreign keys and are connected to the corresponding personal details record.

## Data and Privacy

This application handles personally identifiable information. Use it only with appropriate consent, protect the Neon connection string, restrict database access, and avoid using real personal data in development or testing environments unless proper safeguards are in place.