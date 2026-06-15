from src.services.review_service import get_review, list_risks
from src.utils.formatters import risk_level_text, clause_type_text, review_status_text
from src.constants.risk import ReviewStatus
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

def export_report(review_id: int) -> str:
    logger.info(LOG_TEMPLATES["REPORT_EXPORT"].format(review_id=review_id))
    review = get_review(review_id)
    risk_data = list_risks(review_id)
    groups = risk_data["groups"]
    summary = risk_data["summary"]
    
    lines = [
        f"审查报告 #{review_id}",
        f"有效风险等级：{risk_level_text(summary['effective_risk_level'])}",
        f"概览：共 {summary['total']} 条风险，确认 {summary['confirmed']} 条，待定 {summary['pending']} 条，忽略 {summary['ignored']} 条（已忽略不计入风险等级）",
        "",
        review["summary"],
        ""
    ]
    
    status_order = [ReviewStatus.CONFIRMED, ReviewStatus.PENDING, ReviewStatus.IGNORED]
    for status in status_order:
        status_key = status.value
        items = groups.get(status_key, [])
        if items:
            lines.append(f"【{review_status_text(status)}】({len(items)}条)")
            for item in items:
                lines.append(f"- {clause_type_text(item['clause_type'])} [{risk_level_text(item['risk_level'])}]: {item['description']} / {item['suggestion']}")
            lines.append("")
    
    return "\n".join(lines)

