import logging


def setup_logger():
    logger = logging.getLogger("document_ai")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s |%(levelname)s | %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    return logger


logger = setup_logger()
