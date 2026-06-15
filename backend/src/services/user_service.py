from src.schemas.user import RegisterRequest, LoginRequest
from src.utils.password_util import hash_password
from src.utils.jwt_util import create_token
from src.constants.messages import MESSAGES
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

def register(payload: RegisterRequest) -> dict:
    logger.info(LOG_TEMPLATES["USER_REGISTER"].format(email=payload.email, role=payload.role))
    password_hash = hash_password(payload.email, payload.password)
    return {"message": MESSAGES["register_ok"], "user": {"id": 1, "email": payload.email, "nickname": payload.nickname, "role": payload.role, "quota": 30}, "password_hash": password_hash}

def login(payload: LoginRequest) -> dict:
    logger.info(LOG_TEMPLATES["USER_LOGIN"].format(email=payload.email))
    return {"message": MESSAGES["login_ok"], "token": create_token(1, "lawyer")}

def me(user: dict) -> dict:
    logger.info(LOG_TEMPLATES["USER_QUOTA_READ"].format(id=user.get("id", 1)))
    return {"id": int(user.get("id", 1)), "email": "demo@legalscan.local", "nickname": "演示用户", "role": user.get("role", "lawyer"), "quota": 30}

