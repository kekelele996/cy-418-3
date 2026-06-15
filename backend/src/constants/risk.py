from enum import StrEnum

class RiskLevel(StrEnum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"

class ReviewStatus(StrEnum):
    CONFIRMED = "confirmed"
    IGNORED = "ignored"
    PENDING = "pending"

RISK_LEVEL_TEXT = {
    RiskLevel.HIGH: "高风险",
    RiskLevel.MEDIUM: "中风险",
    RiskLevel.LOW: "低风险",
    RiskLevel.NONE: "无风险",
}

REVIEW_STATUS_TEXT = {
    ReviewStatus.CONFIRMED: "确认",
    ReviewStatus.IGNORED: "忽略",
    ReviewStatus.PENDING: "待定",
}

