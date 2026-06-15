from src.services.review_service import get_review, list_risks
from src.utils.formatters import risk_level_text, clause_type_text
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

def export_report(review_id: int) -> str:
    logger.info(LOG_TEMPLATES["REPORT_EXPORT"].format(review_id=review_id))
    review = get_review(review_id)
    risks = list_risks(review_id)
    lines = [f"审查报告 #{review_id}", f"风险等级：{risk_level_text(review['risk_level'])}", review["summary"]]
    for item in risks:
        lines.append(f"- {clause_type_text(item['clause_type'])}: {item['description']} / {item['suggestion']}")
    return "\n".join(lines)

