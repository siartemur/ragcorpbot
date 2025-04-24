from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat, admin_upload, auth
from app.config.logger_config import setup_logger

app = FastAPI(
    title="RAGCorpBot",
    description="Corporate Knowledge Access Assistant",
    version="1.0.0"
)

# Logger
logger = setup_logger("main")
logger.info("🚀 RAGCorpBot API is starting...")

# CORS configuration (can be separated for dev/prod environments)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/")
def root():
    return {"message": "✅ RAGCorpBot API is active."}

# Routers
app.include_router(chat.router, tags=["Chat"])
app.include_router(admin_upload.router, tags=["Admin"])
app.include_router(auth.router, tags=["Auth"])
