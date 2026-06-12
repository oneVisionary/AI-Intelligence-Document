import requests

BASE_URL = "http://127.0.0.1:8000"


def upload_document(file):
    response = requests.post(f"{BASE_URL}/documents/", files={"file": file})
    response.raise_for_status()
    return response.json()


def get_document_status(document_id):
    response = requests.get(f"{BASE_URL}/documents/{document_id}")
    response.raise_for_status()
    return response.json()


def get_all_document():
    response = requests.get(f"{BASE_URL}/documents")
    response.raise_for_status()
    return response.json()
