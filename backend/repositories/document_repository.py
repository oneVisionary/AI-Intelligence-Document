from models.document import Document
from sqlalchemy.orm import Session


class DocumentRepository:
    def create_document(self, db: Session, document: Document) -> Document:
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    def get_document_by_id(self, db: Session, document_id: str) -> Document | None:
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
