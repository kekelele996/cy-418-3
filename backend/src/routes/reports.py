from fastapi import APIRouter, Depends, Response
from src.controllers.report_controller import export
from src.middlewares.auth_middleware import require_auth

router = APIRouter(prefix="/api/reports", tags=["reports"])

@router.get("/{review_id}/export")
def export_report(review_id: int, user: dict = Depends(require_auth)):
    return Response(export(review_id), media_type="text/plain; charset=utf-8")

