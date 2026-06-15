from src.utils.text_extractor import extract_text
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

def parse_document(document_id: int, file_path: str, file_type: str) -> str:
    logger.info(LOG_TEMPLATES["DOCUMENT_PARSE_START"].format(id=document_id, file_type=file_type))
    text = extract_text(file_path, file_type)
    logger.info(LOG_TEMPLATES["DOCUMENT_PARSE_DONE"].format(id=document_id))
    return text

