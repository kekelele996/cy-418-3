from fastapi import FastAPI
from src.config.database import Base, engine
from src.middlewares.audit_middleware import AuditMiddleware
from src.middlewares.rate_limit_middleware import RateLimitMiddleware
from src.middlewares.error_handler_middleware import global_exception_handler
from src.routes import auth, users, documents, reviews, reports

app = FastAPI(title="LegalScan API", version="1.0.0")
app.add_middleware(AuditMiddleware)
app.add_middleware(RateLimitMiddleware)
app.add_exception_handler(Exception, global_exception_handler)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(documents.router)
app.include_router(reviews.router)
app.include_router(reports.router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok", "service": "legalscan"}

