from datetime import datetime, timedelta, timezone
from jose import jwt
from src.config.app import JWT_SECRET, JWT_EXPIRES_MINUTES
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

ALGORITHM = "HS256"

def create_token(user_id: int, role: str) -> str:
    logger.info(LOG_TEMPLATES["JWT_SIGN"].format(user_id=user_id, role=role))
    payload = {"sub": str(user_id), "role": role, "exp": datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRES_MINUTES)}
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)

def verify_token(token: str) -> dict:
    logger.info(LOG_TEMPLATES["JWT_VERIFY"])
    return jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])

