from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

def extract_text(file_path: str, file_type: str) -> str:
    logger.info(LOG_TEMPLATES["TEXT_EXTRACT"].format(file_type=file_type))
    if file_type == "txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as fh:
            return fh.read()
    return "合同文本示例：付款逾期需要承担违约责任，知识产权归属需明确，争议提交仲裁。"

