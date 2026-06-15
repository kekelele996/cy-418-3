import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from src.config.rate_limit import RATE_LIMITS
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

BUCKETS: dict[str, list[float]] = {}

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        key = request.client.host + ":" + request.url.path if request.client else request.url.path
        config = RATE_LIMITS["login"] if "login" in request.url.path else RATE_LIMITS.get("review_submit", {"window": 60, "limit": 200})
        now = time.time()
        BUCKETS[key] = [item for item in BUCKETS.get(key, []) if now - item < config["window"]]
        if len(BUCKETS[key]) >= config["limit"]:
            logger.warning(LOG_TEMPLATES["RATE_LIMIT_HIT"].format(key=key))
            return JSONResponse({"message": f"Request[path={request.url.path}] rate failed: key {key}"}, status_code=429)
        BUCKETS[key].append(now)
        return await call_next(request)

