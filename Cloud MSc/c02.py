#   Create a google form which contain student information

from googleapiclient.discovery import build
from google.oauth2 import service_account

# Replace these values with your specific details
SCOPES = ["https://www.googleapis.com/auth/forms"]
SERVICE_ACCOUNT_FILE = "path/to/your/credentials.json"
FORM_TITLE = "Student Information Form"
FIELDS = ["Name", "Roll Number", "Email", "Major"]


def create_google_form():
    # Authenticate with Google Forms API using service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("forms", "v1", credentials=credentials)

    # Create a new form
    form = service.forms().create(body={"title": FORM_TITLE}).execute()
    form_id = form["formId"]

    # Add form fields
    for field in FIELDS:
        service.forms().update(
            formId=form_id, body={"title": field, "type": "TEXT"}, fields="title,type"
        ).execute()

    print(f"Google Form created successfully. Form ID: {form_id}")


if _name_ == "_main_":
    create_google_form()
