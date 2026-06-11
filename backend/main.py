from fastapi import FastAPI

from api.documents import router

app = FastAPI(title="AI intellgent document")
app.include_router(router)

# uvicorn main:app --reload
