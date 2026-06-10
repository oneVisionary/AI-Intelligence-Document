
from models.document import Document
from sqlalchemy.orm import Session
class DocumentRepository:
    def create_document(self, db:Session ,document:Document)->Document:
        db.add(document)
        db.commit()
        db.refresh(document)
        return document
    
    def get_document_by_id(self,db:Session, document_id:str)->Document|None:
        document_data = db.query(Document).filter(Document.document_id== document_id).first()
        return document_data
    
    def get_all_documents(self, db:Session):
        document_list = db.query(Document).all()
        return document_list
