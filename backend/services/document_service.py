from repositories.document_repository import DocumentRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.document import Document
from schemas.document import DocumentCreate
from core.logging import logger

import uuid


class DocumentService:

    def __init__(self):
        self.document_repository = DocumentRepository()

    def document_create(self, db: Session, document_data: DocumentCreate):

        try:

            logger.info(f"Creating document: {document_data.original_filename}")

            document = Document(
                document_id=f"DOC-{uuid.uuid4().hex[:8]}",
                original_filename=document_data.original_filename,
                file_path=document_data.file_path,
                file_type=document_data.file_type,
                file_size=document_data.file_size,
            )

            created_document = self.document_repository.create_document(db, document)

            logger.info(
                f"Document created successfully: " f"{created_document.document_id}"
            )

            return created_document

        except Exception as e:

            logger.error(f"Document creation failed: {str(e)}")

            raise HTTPException(status_code=500, detail="Failed to create document")

    def get_document(self, db: Session, document_id: str):

        try:

            document = self.document_repository.get_document_by_id(db, document_id)

        except Exception as e:

            logger.error(f"Failed to fetch document: {str(e)}")

            raise HTTPException(status_code=500, detail="Failed to fetch document")

        if not document:

            logger.warning(f"Document not found: {document_id}")

            raise HTTPException(status_code=404, detail="Document not found")

        return document

    def get_all_documents(self, db: Session):

        try:

            logger.info("Fetching all documents")

            documents = self.document_repository.get_all_documents(db)

            logger.info(f"Retrieved {len(documents)} documents")

            return documents

        except Exception as e:

            logger.error(f"Failed to fetch documents: {str(e)}")

            raise HTTPException(status_code=500, detail="Failed to fetch documents")
