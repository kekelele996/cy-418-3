from src.services.risk_engine import scan_text
from src.constants.risk import RiskLevel
from src.constants.messages import MESSAGES
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

def create_review(user: dict, document_id: int) -> dict:
    logger.info(LOG_TEMPLATES["REVIEW_CREATE"].format(document_id=document_id, role=user.get("role", "user")))
    risks = scan_text("付款逾期需要承担违约责任，知识产权归属需明确。")
    highest = RiskLevel.HIGH if any(item["risk_level"] == RiskLevel.HIGH for item in risks) else risks[0]["risk_level"]
    logger.info(LOG_TEMPLATES["REVIEW_DONE"].format(id=1, risk_level=highest.value))
    return {"id": 1, "document_id": document_id, "risk_level": highest, "summary": MESSAGES["risk_found"]}

def get_review(review_id: int) -> dict:
    return {"id": review_id, "document_id": 1, "risk_level": RiskLevel.HIGH, "summary": "付款和违约条款需重点复核"}

def list_risks(review_id: int) -> list[dict]:
    logger.info(LOG_TEMPLATES["RISK_ITEM_FILTER"].format(review_task_id=review_id, clause_type="all", risk_level="all"))
    return scan_text("付款逾期需要承担违约责任，知识产权归属需明确。")

