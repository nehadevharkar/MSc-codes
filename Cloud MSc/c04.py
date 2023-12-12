# Create your resume in a neat format using google and store in drive

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build


def authenticate():
    SCOPES = [
        "https://www.googleapis.com/auth/documents",
        "https://www.googleapis.com/auth/drive.file",
    ]

    # Replace with the path to your service account credentials file
    SERVICE_ACCOUNT_FILE = "path/to/your/credentials.json"

    creds = None
    # The file token.json stores the user's access and refresh tokens and is
    # created automatically when the authorization flow completes for the first time.
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        return creds
    else:
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        return creds


def create_resume():
    # Connect to Google Docs and Drive APIs
    creds = authenticate()
    docs_service = build("docs", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    # Create a new Google Docs document
    document = docs_service.documents().create().execute()
    document_id = document["documentId"]

    # Add content to the document (replace with your resume content)
    content = "Your resume content goes here."
    docs_service.documents().batchUpdate(
        documentId=document_id,
        body={
            "requests": [{"insertText": {"text": content, "location": {"index": 1}}}]
        },
    ).execute()

    # Export the document as a PDF
    pdf_request = {
        "title": "Resume",
        "mimeType": "application/pdf",
    }
    pdf = (
        drive_service.files()
        .export(fileId=document_id, mimeType="application/pdf")
        .execute()
    )
    pdf_content = pdf.getvalue()

    # Save the PDF to Google Drive
    resume_file_metadata = {
        "name": "Resume.pdf",
        "mimeType": "application/pdf",
    }
    resume_file = (
        drive_service.files()
        .create(body=resume_file_metadata, media_body=pdf_content)
        .execute()
    )

    print(f'Resume created and saved to Google Drive. File ID: {resume_file["id"]}')


if __name__ == "__main__":
    create_resume()
