from src.services import review_service
from src.utils.logger import logger

def create(user: dict, document_id: int) -> dict:
    try:
        return review_service.create_review(user, document_id)
    except Exception as exc:
        msg = f"ReviewTask[document_id={document_id}] create failed: user role={user.get('role')}: {exc}"
        logger.error(msg)
        raise

def get(review_id: int) -> dict:
    return review_service.get_review(review_id)

def risks(review_id: int) -> list[dict]:
    return review_service.list_risks(review_id)

