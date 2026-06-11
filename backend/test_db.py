from sqlalchemy import create_engine
from sqlalchemy import text

DATABASE_URL = "postgresql://postgres:root@localhost:5432/document_ai"


try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("select current_database();"))
        print("Database connected successfully")
        for row in result:
            print(f"Database:{row}")
except Exception as e:
    print("Connection failed")
    print(e)

from core.config import settings

print(settings.APP_NAME)
print(settings.REDIS_URL)

from services.nlp_service import NLPServices

service = NLPServices()

summary = service.summarise_text(
    "FastAPI is a modern Python web framework designed for building APIs..."
)

print(summary)
