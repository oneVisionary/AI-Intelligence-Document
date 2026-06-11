from repositories.document_repository import DocumentRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.document import Document

from core.logging import logger

import uuid
from services.extraction_service import ExtractionService
from services.nlp_service import NLPServices

from worker.document_tasks import process_document
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class DocumentService:

    def __init__(self):
        self.document_repository = DocumentRepository()
        # self.extraction_service = ExtractionService()
        # self.nlp_service = NLPServices()

    def document_create(self, db: Session, metadata: dict, file_path: str):

        created_document = None
        try:

            logger.info(f"Creating document: {metadata['original_filename']}")

            document = Document(
                document_id=f"DOC-{uuid.uuid4().hex[:8]}",
                original_filename=metadata["original_filename"],
                file_path=file_path,
                file_type=metadata["file_type"],
                file_size=metadata["file_size"],
            )

            created_document = self.document_repository.create_document(db, document)

            created_document = self.document_repository.update_document_status(
                db, created_document, "processing"
            )
            process_document.delay(created_document.document_id)

            # extracted_text = self.extraction_service.extract_text(
            #     file_path=file_path, file_type=metadata["file_type"]
            # )

            # created_document = self.document_repository.update_extracted_text(
            #     db, created_document, extracted_text
            # )
            # summary = self.nlp_service.summarise_text(extracted_text)
            # created_document = self.document_repository.update_summary(
            #     db, created_document, summary
            # )
            # created_document = self.document_repository.update_document_status(
            #     db, created_document, "completed"
            # )

            # logger.info(
            #     f"Document created successfully: " f"{created_document.document_id}"
            # )

            return created_document

        except Exception:
            if created_document is not None:
                self.document_repository.update_document_status(
                    db, created_document, "failed"
                )

            logger.exception("Document creation failed")

            raise HTTPException(status_code=500, detail="Failed to create document")

    def get_document(self, db: Session, document_id: str):

        try:

            document = self.document_repository.get_document_by_id(db, document_id)

        except Exception:

            logger.exception(f"Failed to fetch document")

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

        except Exception:
            logger.exception(f"Failed to fetch document")

            raise HTTPException(status_code=500, detail="Failed to fetch documents")
