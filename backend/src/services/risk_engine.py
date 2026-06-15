from src.constants.contract import CLAUSE_KEYWORDS, ClauseType
from src.constants.risk import RiskLevel, ReviewStatus
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

def scan_text(text: str) -> list[dict]:
    risks: list[dict] = []
    for clause_type, words in CLAUSE_KEYWORDS.items():
        for word in words:
          pos = text.find(word)
          if pos >= 0:
              risk_level = RiskLevel.HIGH if clause_type in {ClauseType.BREACH, ClauseType.PAYMENT} else RiskLevel.MEDIUM
              logger.info(LOG_TEMPLATES["RISK_ITEM_CREATE"].format(clause_type=clause_type.value, risk_level=risk_level.value))
              risks.append({"id": len(risks) + 1, "clause_type": clause_type, "risk_level": risk_level, "review_status": ReviewStatus.PENDING, "description": f"命中关键词 {word}", "suggestion": "建议补充责任边界、期限和举证要求。", "start_pos": pos, "end_pos": pos + len(word)})
    return risks or [{"id": 1, "clause_type": ClauseType.OTHER, "risk_level": RiskLevel.NONE, "review_status": ReviewStatus.PENDING, "description": "未发现明显风险", "suggestion": "保持人工复核。", "start_pos": 0, "end_pos": 0}]

