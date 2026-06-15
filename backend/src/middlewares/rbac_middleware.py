from fastapi import HTTPException
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

def require_role(user: dict, roles: set[str]) -> None:
    role = user.get("role", "user")
    if role not in roles:
        logger.warning(LOG_TEMPLATES["RBAC_DENY"].format(role=role, path="api"))
        raise HTTPException(status_code=403, detail=f"User[role={role}] access failed: role not allowed")

