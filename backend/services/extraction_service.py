from core.logging import logger
import fitz
from PIL import Image
import pytesseract


class ExtractionService:
    def extract_pdf(self, file_path: str) -> str:
        try:
            logger.info(f"Start PDF extraction:{file_path}")
            pdf_document = fitz.open(file_path)
            extracted_text = ""
            for page in pdf_document:
                extracted_text += page.get_text()
            pdf_document.close()

            logger.info("PDF extraction completed")
            return extracted_text
        except Exception:
            logger.exception("PDF failed")
            raise

    def extract_image_text(self, file_path: str) -> str:
        try:
            logger.info(f"Start Image extraction:{file_path}")
            image = Image.open(file_path)
            extracted_text = pytesseract.image_to_string(image)

            logger.info("Image OCR completed")
            return extracted_text
        except Exception:
            logger.exception("Image OCR failed")
            raise

    def extract_text(self, file_path: str, file_type: str) -> str:
        if file_type == "pdf":
            return self.extract_pdf(file_path)
        return self.extract_image_text(file_path)
