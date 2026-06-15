from starlette.middleware.base import BaseHTTPMiddleware
from src.services.audit_log_service import write_audit

class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        if request.method in {"POST", "PUT", "PATCH", "DELETE"}:
            write_audit(0, request.method + " " + request.url.path, f"status={response.status_code}")
        return response

