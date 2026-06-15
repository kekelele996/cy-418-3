from src.services.report_generator import export_report
from src.utils.logger import logger

def export(review_id: int) -> str:
    try:
        return export_report(review_id)
    except Exception as exc:
        msg = f"Report[review_id={review_id}] export failed: review_id field invalid: {exc}"
        logger.error(msg)
        raise

