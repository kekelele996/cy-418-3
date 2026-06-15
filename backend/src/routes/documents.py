from fastapi import APIRouter, Depends, Form
from src.controllers import document_controller
from src.middlewares.auth_middleware import require_auth

router = APIRouter(prefix="/api/documents", tags=["documents"])

@router.post("")
def create_document(title: str = Form("采购合同.txt"), file_type: str = Form("txt"), file_size: int = Form(2048), user: dict = Depends(require_auth)):
    return document_controller.create(user, title, file_type, file_size)

@router.get("")
def list_documents(user: dict = Depends(require_auth)):
    return document_controller.list_all()

@router.get("/{document_id}")
def get_document(document_id: int, user: dict = Depends(require_auth)):
    return document_controller.get(document_id)

