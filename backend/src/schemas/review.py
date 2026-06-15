from pydantic import BaseModel
from src.constants.risk import RiskLevel, ReviewStatus
from src.constants.contract import ClauseType

class ReviewCreate(BaseModel):
    document_id: int

class ReviewStatusUpdate(BaseModel):
    review_status: ReviewStatus

class RiskItemOut(BaseModel):
    id: int
    clause_type: ClauseType
    risk_level: RiskLevel
    review_status: ReviewStatus
    description: str
    suggestion: str

class ReviewOut(BaseModel):
    id: int
    document_id: int
    risk_level: RiskLevel
    summary: str

