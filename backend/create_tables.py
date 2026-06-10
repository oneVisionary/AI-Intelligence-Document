from models.document import Document
from core.database import Base, engine

Base.metadata.create_all(bind=engine)
print("Table created Successfully")
