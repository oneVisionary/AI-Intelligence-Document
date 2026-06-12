from models.document import Document
from sqlalchemy.orm import Session
from datetime import datetime, UTC


class DocumentRepository:
    def create_document(self, db: Session, document: Document) -> Document:
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    def get_document_by_id(self, db: Session, document_id: str) -> Document | None:
        document_data = (
            db.query(Document).filter(Document.document_id == document_id).first()
        )
        return document_data

    def get_document_by_unique_id(
        self, db: Session, document_id: str
    ) -> Document | None:
        document_data = db.query(Document).filter(Document.id == document_id).first()
        return document_data

    def get_all_documents(self, db: Session):
        document_list = db.query(Document).all()
        return document_list

    def update_extracted_text(
        self, db: Session, document: Document, extracted_text: str
    ):
        document.extracted_text = extracted_text
        db.commit()
        db.refresh(document)
        return document

    def update_summary(self, db: Session, document: Document, summary: str):
        document.summary = summary
        db.commit()
        db.refresh(document)
        return document

    def update_document_status(self, db: Session, document: Document, status: str):
        document.status = status
        db.commit()
        db.refresh(document)
        return document

    def update_ocr_started(self, db: Session, document: Document):
        document.ocr_started_at = datetime.now(UTC)
        db.commit()
        db.refresh(document)
        return document

    def update_ocr_completed(self, db: Session, document: Document):
        document.ocr_completed_at = datetime.now(UTC)
        db.commit()
        db.refresh(document)
        return document

    def update_summary_started(self, db: Session, document: Document):
        document.summary_started_at = datetime.now(UTC)
        db.commit()
        db.refresh(document)
        return document

    def update_summary_completed(self, db: Session, document: Document):
        # 1. Capture the current time with UTC
        completed_at = datetime.now(UTC)
        document.summary_completed_at = completed_at

        # 2. Ensure both datetimes are localized to UTC before doing math
        # This prevents the TypeError regardless of how the DB stored it
        started_at = document.summary_started_at

        if started_at is not None:
            # If started_at is naive, assume it's UTC or convert it to match completed_at
            if started_at.tzinfo is None:
                # If your DB stores as UTC but drops the flag:
                started_at = started_at.replace(tzinfo=UTC)

            # Now they are safe to subtract
            document.processing_time_seconds = (
                completed_at - started_at
            ).total_seconds()
        else:
            document.processing_time_seconds = 0.0

        db.commit()
        db.refresh(document)
        return document
