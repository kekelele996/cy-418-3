from datetime import datetime
from src.constants.risk import RiskLevel, RISK_LEVEL_TEXT
from src.constants.contract import ClauseType

CLAUSE_TYPE_TEXT = {
    ClauseType.BREACH: "违约责任",
    ClauseType.IP: "知识产权",
    ClauseType.CONFIDENTIALITY: "保密",
    ClauseType.DISPUTE: "争议解决",
    ClauseType.PAYMENT: "付款",
    ClauseType.OTHER: "其他",
}

def format_date(value: datetime | None) -> str:
    return value.strftime("%Y-%m-%d %H:%M") if value else "-"

def risk_level_text(level: RiskLevel | str) -> str:
    return RISK_LEVEL_TEXT.get(RiskLevel(level), "未知")

def clause_type_text(clause_type: ClauseType | str) -> str:
    return CLAUSE_TYPE_TEXT.get(ClauseType(clause_type), "其他")

def file_size_text(size: int) -> str:
    return f"{size / 1024:.1f} KB"

def status_text(status: str) -> str:
    return {"pending": "待处理", "processing": "处理中", "done": "已完成", "failed": "失败"}.get(status, status)

