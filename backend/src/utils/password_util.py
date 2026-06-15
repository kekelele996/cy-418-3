import hashlib
import hmac
import os
from src.utils.logger import logger
from src.constants.log_templates import LOG_TEMPLATES

ITERATIONS = 180_000

def hash_password(email: str, password: str) -> str:
    logger.info(LOG_TEMPLATES["PASSWORD_HASH"].format(email=email))
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERATIONS)
    return f"pbkdf2_sha256${ITERATIONS}${salt.hex()}${digest.hex()}"

def verify_password(password: str, hashed: str) -> bool:
    try:
        scheme, iterations, salt_hex, digest_hex = hashed.split("$", 3)
        if scheme != "pbkdf2_sha256":
            return False
        digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), bytes.fromhex(salt_hex), int(iterations))
        return hmac.compare_digest(digest.hex(), digest_hex)
    except Exception:
        return False
