from src.services import document_service
from src.utils.logger import logger

def create(user: dict, title: str, file_type: str, file_size: int) -> dict:
    try:
        return document_service.create_document(user, title, file_type, file_size)
    except Exception as exc:
        msg = f"Document[title={title}] controller failed: file_type={file_type}: {exc}"
        logger.error(msg)
        raise

def list_all() -> list[dict]:
    return document_service.list_documents()

def get(document_id: int) -> dict:
    return document_service.get_document(document_id)

