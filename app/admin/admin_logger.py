import logging

logger = logging.getLogger("admin_logger")
logger.setLevel(logging.INFO)

def log_upload(filename: str):
    logger.info(f"[UPLOAD] {filename} has been uploaded.")

def log_reset():
    logger.info("[RESET] FAISS index and metadata have been cleared.")
