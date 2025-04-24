from pydantic import BaseModel
from typing import Optional

class UploadResponse(BaseModel):
    message: str
    chunk_sayisi: int

class ResetResponse(BaseModel):
    message: str

class UploadErrorResponse(BaseModel):
    detail: str
