import os

APP_NAME = "LegalScan"
JWT_SECRET = os.getenv("JWT_SECRET", "legalscan_dev_secret")
JWT_EXPIRES_MINUTES = int(os.getenv("JWT_EXPIRES_MINUTES", "120"))
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")

