from enum import StrEnum

class ClauseType(StrEnum):
    BREACH = "breach"
    IP = "ip"
    CONFIDENTIALITY = "confidentiality"
    DISPUTE = "dispute"
    PAYMENT = "payment"
    OTHER = "other"

CLAUSE_KEYWORDS = {
    ClauseType.BREACH: ["违约", "赔偿"],
    ClauseType.IP: ["知识产权", "著作权", "专利"],
    ClauseType.CONFIDENTIALITY: ["保密", "秘密"],
    ClauseType.DISPUTE: ["仲裁", "诉讼", "争议"],
    ClauseType.PAYMENT: ["付款", "逾期", "发票"],
    ClauseType.OTHER: ["其他"],
}

