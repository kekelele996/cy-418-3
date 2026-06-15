from fastapi import APIRouter, Depends
from src.controllers.user_controller import profile
from src.middlewares.auth_middleware import require_auth

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/profile")
def get_profile(user: dict = Depends(require_auth)):
    return profile(user)

