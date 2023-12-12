Create a google quiz which contain 5 different types of questions(mcq, true/false, short answer, fill in the blank) and give following types of the setting to your quiz
a. Shuffle Questions
b. Limit to 1 Response

import json
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build

def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/forms']
    SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'

    creds = None
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

def create_google_form():
    creds = authenticate()
    service = build('forms', 'v1', credentials=creds)

    # Create a new form
    form = service.forms().create(body={'title': 'Quiz with Settings'}).execute()
    form_id = form['formId']

    # Add questions
    questions = [
        {
            'type': 'multiple_choice',
            'text': 'What is the capital of France?',
            'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
            'correct_answer': 'Paris'
        },
        {
            'type': 'true_false',
            'text': 'The Earth is flat.',
            'correct_answer': False
        },
        {
            'type': 'short_answer',
            'text': 'What is the capital of Japan?',
            'correct_answer': 'Tokyo'
        },
        {
            'type': 'fill_in_the_blank',
            'text': 'The largest ocean in the world is ____.'
        }
        # Add more questions as needed...
    ]

    for question in questions:
        service.forms().update(
            formId=form_id,
            body={'title': question['text'], 'type': question['type']},
            fields='title,type'
        ).execute()

        if 'options' in question:
            for option in question['options']:
                service.forms().update(
                    formId=form_id,
                    body={'title': option, 'type': 'MULTIPLE_CHOICE'},
                    fields='title,type'
                ).execute()

    # Set form settings
    service.forms().update(
        formId=form_id,
        body={
            'shuffleQuestions': True,
            'allowResponseEdits': False
        },
        fields='shuffleQuestions,allowResponseEdits'
    ).execute()

    print(f'Google Form created successfully. Form ID: {form_id}')

if _name_ == '_main_':
    create_google_form()