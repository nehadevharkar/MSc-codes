Working on Google drive to make Spreadsheets and notes.

import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return creds

def create_spreadsheet(creds, spreadsheet_title):
    drive_service = build('drive', 'v3', credentials=creds)

    spreadsheet_metadata = {
        'name': spreadsheet_title,
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }

    spreadsheet = drive_service.files().create(
        body=spreadsheet_metadata,
        fields='id'
    ).execute()

    print(f'Spreadsheet created. ID: {spreadsheet["id"]}')

def create_note(creds, note_title, note_content):
    drive_service = build('drive', 'v3', credentials=creds)

    note_metadata = {
        'name': note_title,
        'mimeType': 'text/plain'
    }

    media_body = MediaFileUpload(io.StringIO(note_content), mimetype='text/plain')

    note = drive_service.files().create(
        body=note_metadata,
        media_body=media_body,
        fields='id'
    ).execute()

    print(f'Note created. ID: {note["id"]}')

if _name_ == '_main_':
    # Replace with the actual path to your service account credentials file
    creds = authenticate()

    # Create a spreadsheet
    create_spreadsheet(creds, 'My Spreadsheet')

    # Create a note
    create_note(creds, 'My Note', 'This is a sample note content.')