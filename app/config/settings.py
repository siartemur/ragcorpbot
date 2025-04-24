import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Directory and file paths
UPLOAD_DIR = "data/admin_uploads"
INDEX_PATH = "vector_store/index.faiss"
META_PATH = "vector_store/meta.pkl"

# Admin credentials
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

print("[SETTINGS] Environment variables loaded.")
