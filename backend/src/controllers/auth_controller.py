from src.schemas.user import RegisterRequest, LoginRequest
from src.services import user_service
from src.utils.logger import logger

def register(payload: RegisterRequest) -> dict:
    try:
        return user_service.register(payload)
    except Exception as exc:
        msg = f"User[email={payload.email}] register failed: role {payload.role}: {exc}"
        logger.error(msg)
        raise

def login(payload: LoginRequest) -> dict:
    try:
        return user_service.login(payload)
    except Exception as exc:
        msg = f"User[email={payload.email}] login failed: password invalid: {exc}"
        logger.error(msg)
        raise

def me(user: dict) -> dict:
    return user_service.me(user)

