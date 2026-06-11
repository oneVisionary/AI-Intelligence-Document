from core.logging import logger
from transformers import pipeline
import ollama


class NLPServices:
    def __init__(self):
        logger.info("Loading Ollama summarization model")

    def summarise_text(self, text: str) -> str:
        try:
            logger.info("Starting summarization")
            if len(text.strip()) == 0:
                return ""

            response = ollama.chat(
                model="llama3.2:1b",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
Summarize the following document in a concise paragraph:

{text[:3000]}
""",
                    }
                ],
            )

            logger.info(" summarization completed")
            return response["message"]["content"]
        except Exception:
            logger.exception("Summarization failed")
            raise
