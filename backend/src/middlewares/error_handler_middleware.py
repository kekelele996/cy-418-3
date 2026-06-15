from fastapi import Request
from fastapi.responses import JSONResponse
from src.constants.error_codes import ERROR_CODES
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

async def global_exception_handler(request: Request, exc: Exception):
    logger.error(LOG_TEMPLATES["MIDDLEWARE_ERROR"].format(name="error_handler", error=str(exc)))
    return JSONResponse(status_code=500, content={"code": ERROR_CODES["REVIEW_FAILED"], "message": str(exc), "path": request.url.path})

