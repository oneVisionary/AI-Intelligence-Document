from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from core.dependencies import get_db

from services.document_service import DocumentService

from schemas.document import (DocumentCreate, DocumentUploadResponse)


router = APIRouter(prefix="/documents", tags =["Documents"])
document_services = DocumentService()



@router.post("/", response_model = DocumentUploadResponse)
def create_document(document_data:DocumentCreate, db:Session= Depends(get_db)):
    return document_services.document_create(db, document_data)


@router.get("/")
def get_all_document( db:Session= Depends(get_db)):
    return document_services.get_all_documents(db)


@router.get("/{document_id}")
def get_document(document_id:str, db:Session= Depends(get_db)):
    return document_services.get_document(db, document_id)