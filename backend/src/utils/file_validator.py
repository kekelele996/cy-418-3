from src.constants.error_codes import ERROR_CODES
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

ALLOWED_TYPES = {"pdf", "docx", "txt"}
MAX_SIZE = 20 * 1024 * 1024

def validate_file(name: str, size: int, file_type: str) -> None:
    logger.info(LOG_TEMPLATES["FILE_VALIDATE"].format(name=name, size=size))
    if file_type not in ALLOWED_TYPES:
        reason = f"Document[file_type={file_type}] invalid: {ERROR_CODES['DOCUMENT_UNSUPPORTED']}"
        logger.error(LOG_TEMPLATES["FILE_VALIDATE_FAILED"].format(name=name, reason=reason))
        raise ValueError(reason)
    if size > MAX_SIZE:
        raise ValueError(f"Document[file_size={size}] invalid: {ERROR_CODES['DOCUMENT_TOO_LARGE']}")

