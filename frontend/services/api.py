import requests

BASE_URL = "http://127.0.0.1:8000"


def upload_document(file):
    response = requests.post(f"{BASE_URL}/documents/", files={"file": file})
    return response.json()


def get_document_status(document_id):
    response = requests.get(f"{BASE_URL}/documents/{document_id}")
    return response.json()
