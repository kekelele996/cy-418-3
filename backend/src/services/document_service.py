from src.utils.file_validator import validate_file
from src.constants.messages import MESSAGES
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

def create_document(user: dict, title: str, file_type: str, file_size: int) -> dict:
    try:
        validate_file(title, file_size, file_type)
        logger.info(LOG_TEMPLATES["DOCUMENT_UPLOAD"].format(title=title, file_type=file_type, role=user.get("role", "user")))
        return {"id": 1, "title": title, "file_type": file_type, "file_size": file_size, "status": "pending", "message": MESSAGES["document_uploaded"]}
    except Exception as exc:
        message = f"Document[title={title}] create failed: file_type {file_type} invalid for role={user.get('role', 'user')}: {exc}"
        logger.error(LOG_TEMPLATES["DOCUMENT_UPLOAD_FAILED"].format(title=title, reason=message))
        raise ValueError(message) from exc

def list_documents() -> list[dict]:
    return [{"id": 1, "title": "采购合同.txt", "file_type": "txt", "file_size": 2048, "status": "done"}]

def get_document(document_id: int) -> dict:
    logger.info(LOG_TEMPLATES["DOCUMENT_STATUS"].format(id=document_id))
    return {"id": document_id, "title": "采购合同.txt", "file_type": "txt", "file_size": 2048, "status": "done"}

