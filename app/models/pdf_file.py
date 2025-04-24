from dataclasses import dataclass
from datetime import datetime

@dataclass
class PDFFile:
    filename: str
    upload_time: datetime
    chunk_count: int
