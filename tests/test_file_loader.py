import os
from app.services.file_loader_service import load_pdf_chunks

def test_pdf_loading():
    test_path = "data/admin_uploads/example.pdf"
    chunks = load_pdf_chunks(test_path)
    assert len(chunks) > 0
    assert all(chunk.content for chunk in chunks)
    assert all(chunk.page_number > 0 for chunk in chunks)
