from worker.celery_app import celery_app
from datetime import datetime

from services.extraction_service import ExtractionService
from services.nlp_service import NLPServices
from repositories.document_repository import DocumentRepository

from core.database import SessionLocal
from core.logging import logger

extraction_service = ExtractionService()
nlp_service = NLPServices()
document_repository = DocumentRepository()


@celery_app.task
def process_document(document_id: str):

    db = SessionLocal()

    try:

        logger.info(f"Processing document: {document_id}")

        document = document_repository.get_document_by_id(db, document_id)

        if not document:

            logger.error(f"Document not found: {document_id}")

            return
        # ocr start

        document_repository.update_ocr_started(db, document)
        extracted_text = extraction_service.extract_text(
            file_path=document.file_path,
            file_type=document.file_type,
        )

        document_repository.update_extracted_text(
            db,
            document,
            extracted_text,
        )
        document_repository.update_ocr_completed(db, document)
        document_repository.update_summary_started(db, document)
        summary = nlp_service.summarise_text(extracted_text)

        document_repository.update_summary(
            db,
            document,
            summary,
        )

        document_repository.update_document_status(
            db,
            document,
            "completed",
        )
        document_repository.update_summary_completed(db, document)
        logger.info(f"Processing completed: {document_id}")

    except Exception:

        logger.exception(f"Processing failed: {document_id}")

        if document:

            document_repository.update_document_status(
                db,
                document,
                "failed",
            )

    finally:

        db.close()
