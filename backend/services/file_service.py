import os
import uuid
from fastapi import UploadFile


class FileService:

    def validate_file(self, file: UploadFile):
        allowed_extensions = ["pdf", "png", "jpeg", "jpg"]
        if "." not in file.filename:
            raise ValueError("File has no extension")
        file_extension = file.filename.split(".")[-1].lower()
        if file_extension not in allowed_extensions:
            raise ValueError(f"unsupported file type:{file_extension}")
        return file_extension

    def extract_metadata(self, file: UploadFile):
        file_extension = self.validate_file(file)
        file.file.seek(0)
        file_content = file.file.read()
        file_size = len(file_content)
        file.file.seek(0)
        return {
            "original_filename": file.filename,
            "file_type": file_extension,
            "file_size": file_size,
        }

    def save_file(self, file: UploadFile, upload_dir: str):
        unique_filename = f"{uuid.uuid4().hex}_{file.filename}"
        file_path = os.path.join(upload_dir, unique_filename)
        file.file.seek(0)
        file_content = file.file.read()
        with open(file_path, "wb") as buffer:
            buffer.write(file_content)
        file.file.seek(0)
        return file_path
