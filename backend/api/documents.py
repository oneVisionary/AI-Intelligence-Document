from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from core.dependencies import get_db
from core.config import settings
from services.document_service import DocumentService
from services.file_service import FileService
from schemas.document import DocumentUploadResponse

router = APIRouter(prefix="/documents", tags=["Documents"])
document_services = DocumentService()

file_services = FileService()


@router.post("/", response_model=DocumentUploadResponse)
def create_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    meta_data = file_services.extract_metadata(file)
    file_path = file_services.save_file(file, settings.UPLOAD_DIR)
    return document_services.document_create(db, meta_data, file_path)


@router.get("/")
def get_all_document(db: Session = Depends(get_db)):
    return document_services.get_all_documents(db)


@router.get("/{document_id}")
def get_document(document_id: str, db: Session = Depends(get_db)):

    print("Requested ID:", document_id)

    result = document_services.get_document_by_uniqueid(db, document_id)

    print("Result:", result)

    return result
