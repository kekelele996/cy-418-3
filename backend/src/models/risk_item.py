from sqlalchemy import String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from src.config.database import Base
from src.constants.contract import ClauseType
from src.constants.risk import RiskLevel

class RiskItem(Base):
    __tablename__ = "risk_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    review_task_id: Mapped[int] = mapped_column(ForeignKey("review_tasks.id"))
    clause_type: Mapped[str] = mapped_column(String(32), default=ClauseType.OTHER.value)
    risk_level: Mapped[str] = mapped_column(String(32), default=RiskLevel.LOW.value)
    description: Mapped[str] = mapped_column(Text)
    suggestion: Mapped[str] = mapped_column(Text)
    start_pos: Mapped[int] = mapped_column(Integer, default=0)
    end_pos: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

