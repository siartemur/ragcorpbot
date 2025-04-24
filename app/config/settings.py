import os
from dotenv import load_dotenv

load_dotenv()

# API anahtarı
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Dosya yolları
UPLOAD_DIR = "data/admin_uploads"
INDEX_PATH = "vector_store/index.faiss"
META_PATH = "vector_store/meta.pkl"

# Admin bilgileri
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

# DEBUG: Ortam değişkenlerinin başarıyla yüklendiğini görmek için
print("[SETTINGS] Ortam değişkenleri yüklendi.")
