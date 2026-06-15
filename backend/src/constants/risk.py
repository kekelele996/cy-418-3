from enum import StrEnum

class RiskLevel(StrEnum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"

RISK_LEVEL_TEXT = {
    RiskLevel.HIGH: "高风险",
    RiskLevel.MEDIUM: "中风险",
    RiskLevel.LOW: "低风险",
    RiskLevel.NONE: "无风险",
}

