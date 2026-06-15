from fastapi import APIRouter, Depends
from src.schemas.user import RegisterRequest, LoginRequest
from src.controllers import auth_controller
from src.middlewares.auth_middleware import require_auth

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register")
def register(payload: RegisterRequest):
    return auth_controller.register(payload)

@router.post("/login")
def login(payload: LoginRequest):
    return auth_controller.login(payload)

@router.get("/me")
def me(user: dict = Depends(require_auth)):
    return auth_controller.me(user)

