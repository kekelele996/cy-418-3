from fastapi import APIRouter, Depends
from src.schemas.review import ReviewCreate
from src.controllers import review_controller
from src.middlewares.auth_middleware import require_auth

router = APIRouter(prefix="/api/reviews", tags=["reviews"])

@router.post("")
def create_review(payload: ReviewCreate, user: dict = Depends(require_auth)):
    return review_controller.create(user, payload.document_id)

@router.get("/{review_id}")
def get_review(review_id: int, user: dict = Depends(require_auth)):
    return review_controller.get(review_id)

@router.get("/{review_id}/risks")
def get_risks(review_id: int, user: dict = Depends(require_auth)):
    return review_controller.risks(review_id)

