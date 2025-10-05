# Pydantic Contact Form Validator

This is a simple web application built with Streamlit and Pydantic to demonstrate data validation for a contact form.

## About the Project

This project allows users to submit contact information (Name, Email, Age, and Phone Number) through a web form. The backend uses Pydantic to validate the data according to a set of rules:
-   **Name**: Must be a string with a minimum length.
-   **Email**: Must be a valid email format.
-   **Age**: Must be a positive integer.
-   **Phone Number**: Must be a 10-digit number.

Valid submissions are saved to an Excel file (`data/contacts.xlsx`).

## Setup

To run this project locally, you will need to have Python installed.

1.  **Clone the repository (or download the source code).**

2.  **Create and activate a virtual environment:**
    ```bash
    # Create a virtual environment
    python -m venv myenv

    # Activate on Windows
    myenv\Scripts\activate

    # Activate on macOS/Linux
    source myenv/bin/activate
    ```

3.  **Install the required dependencies:**
    All the necessary libraries are listed in the `requirements.txt` file. Install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Once the setup is complete, you can run the Streamlit application with the following command:

```bash
streamlit run app.py
```

Your web browser should automatically open with the application running.
