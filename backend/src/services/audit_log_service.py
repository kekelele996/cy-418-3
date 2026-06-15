from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

def write_audit(actor_id: int, action: str, detail: str) -> None:
    logger.info(LOG_TEMPLATES["AUDIT_WRITE"].format(action=action, actor_id=actor_id) + " " + detail)

