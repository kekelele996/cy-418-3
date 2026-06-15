from src.config.celery import celery_app
from src.services.review_service import create_review
from src.constants.log_templates import LOG_TEMPLATES
from src.utils.logger import logger

@celery_app.task
def run_review_task(review_task_id: int, document_id: int):
    logger.info(LOG_TEMPLATES["CELERY_SUBMIT"].format(review_task_id=review_task_id))
    result = create_review({"id": 0, "role": "worker"}, document_id)
    logger.info(LOG_TEMPLATES["CELERY_DONE"].format(review_task_id=review_task_id))
    return result

