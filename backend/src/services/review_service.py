from datetime import datetime
from src.services.risk_engine import scan_text
from src.constants.risk import RiskLevel, ReviewStatus
from src.constants.messages import MESSAGES
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

_risks_store = {}

def _get_risks(review_id: int) -> list[dict]:
    if review_id not in _risks_store:
        _risks_store[review_id] = scan_text("付款逾期需要承担违约责任，知识产权归属需明确。")
    return _risks_store[review_id]

def _calculate_risk_level(risks: list[dict]) -> RiskLevel:
    non_ignored = [r for r in risks if r["review_status"] != ReviewStatus.IGNORED]
    if not non_ignored:
        return RiskLevel.NONE
    if any(item["risk_level"] == RiskLevel.HIGH for item in non_ignored):
        return RiskLevel.HIGH
    if any(item["risk_level"] == RiskLevel.MEDIUM for item in non_ignored):
        return RiskLevel.MEDIUM
    if any(item["risk_level"] == RiskLevel.LOW for item in non_ignored):
        return RiskLevel.LOW
    return RiskLevel.NONE

def _group_risks_by_status(risks: list[dict]) -> dict:
    grouped = {
        ReviewStatus.CONFIRMED: [],
        ReviewStatus.PENDING: [],
        ReviewStatus.IGNORED: []
    }
    for risk in risks:
        status = risk.get("review_status", ReviewStatus.PENDING)
        if status in grouped:
            grouped[status].append(risk)
    return grouped

def create_review(user: dict, document_id: int) -> dict:
    logger.info(LOG_TEMPLATES["REVIEW_CREATE"].format(document_id=document_id, role=user.get("role", "user")))
    risks = _get_risks(1)
    highest = _calculate_risk_level(risks)
    logger.info(LOG_TEMPLATES["REVIEW_DONE"].format(id=1, risk_level=highest.value))
    return {"id": 1, "document_id": document_id, "risk_level": highest, "summary": MESSAGES["risk_found"]}

def get_review(review_id: int) -> dict:
    risks = _get_risks(review_id)
    risk_level = _calculate_risk_level(risks)
    return {"id": review_id, "document_id": 1, "risk_level": risk_level, "summary": "付款和违约条款需重点复核"}

def list_risks(review_id: int) -> dict:
    logger.info(LOG_TEMPLATES["RISK_ITEM_FILTER"].format(review_task_id=review_id, clause_type="all", risk_level="all"))
    risks = _get_risks(review_id)
    grouped = _group_risks_by_status(risks)
    summary = {
        "total": len(risks),
        "confirmed": len(grouped[ReviewStatus.CONFIRMED]),
        "pending": len(grouped[ReviewStatus.PENDING]),
        "ignored": len(grouped[ReviewStatus.IGNORED]),
        "effective_risk_level": _calculate_risk_level(risks)
    }
    return {"summary": summary, "groups": {k.value: v for k, v in grouped.items()}}

def update_risk_status(review_id: int, risk_id: int, status: ReviewStatus) -> dict:
    logger.info(LOG_TEMPLATES["RISK_ITEM_UPDATE"].format(risk_item_id=risk_id, review_status=status.value))
    risks = _get_risks(review_id)
    for risk in risks:
        if risk["id"] == risk_id:
            risk["review_status"] = status
            risk["reviewed_at"] = datetime.utcnow()
            return risk
    raise ValueError(f"Risk item {risk_id} not found")

