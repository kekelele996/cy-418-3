import os
from celery import Celery

celery_app = Celery("legalscan", broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"), backend=os.getenv("REDIS_URL", "redis://localhost:6379/0"))

