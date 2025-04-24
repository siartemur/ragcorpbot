import os
from fastapi import APIRouter, UploadFile, File, Request, Depends, HTTPException
from slugify import slugify

from app.services.file_loader_service import load_pdf_chunks
from app.services.embedding_service import get_chunk_embeddings
from app.repositories.vector_repository import VectorRepository
from app.core.deps import verify_admin
from app.config.settings import UPLOAD_DIR
from app.admin.admin_logger import log_upload, log_reset

router = APIRouter()

@router.post("/admin/upload")
async def upload_pdf(
    request: Request,
    file: UploadFile = File(...),
    _: None = Depends(verify_admin)  # Admin verification
):
    # Format check
    if not file.filename.lower().endswith(".pdf"):
        file.filename += ".pdf"  # Auto-fix if missing .pdf

    # Ensure upload directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Sanitize filename (remove spaces etc.)
    safe_filename = slugify(file.filename)

    # Build file path
    file_path = os.path.join(UPLOAD_DIR, safe_filename)

    # Save file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Split PDF into chunks
    try:
        chunks = load_pdf_chunks(file_path)
        if not chunks:
            raise HTTPException(status_code=400, detail="Unable to extract content from PDF.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chunking error: {str(e)}")

    # Generate embeddings & save to FAISS
    try:
        embeddings = get_chunk_embeddings(chunks)
        repo = VectorRepository()
        repo.add_embeddings(embeddings, chunks)
        log_upload(safe_filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding error: {str(e)}")

    return {
        "message": f"{file.filename} uploaded and processed successfully.",
        "chunk_count": len(chunks)
    }

@router.post("/admin/reset")
async def reset_faiss(_: None = Depends(verify_admin)):
    try:
        repo = VectorRepository()
        repo.reset_index()
        log_reset()
        return {"message": "FAISS index and metadata were successfully cleared."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Reset error: {str(e)}")
