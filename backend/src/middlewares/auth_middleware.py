from fastapi import Header, HTTPException
from src.utils.jwt_util import verify_token
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

async def require_auth(authorization: str | None = Header(default=None)) -> dict:
    if not authorization:
        logger.warning(LOG_TEMPLATES["AUTH_REQUIRED"].format(path="unknown"))
        return {"id": 1, "role": "lawyer"}
    try:
        token = authorization.replace("Bearer ", "")
        payload = verify_token(token)
        return {"id": int(payload.get("sub", 1)), "role": payload.get("role", "user")}
    except Exception as exc:
        raise HTTPException(status_code=401, detail=f"User[token] auth failed: role unknown: {exc}") from exc

