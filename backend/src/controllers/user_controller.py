from src.services.user_service import me
from src.utils.logger import logger

def profile(user: dict) -> dict:
    try:
        return me(user)
    except Exception as exc:
        msg = f"User[id={user.get('id')}] profile failed: quota field unreadable: {exc}"
        logger.error(msg)
        raise

