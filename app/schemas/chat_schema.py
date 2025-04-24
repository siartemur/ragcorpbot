from pydantic import BaseModel, Field
from typing import Optional, List

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=5, max_length=500, description="The question the user wants to ask GPT.")

class ChatResponse(BaseModel):
    answer: str
    sources: Optional[List[str]] = None 
    confidence: Optional[float] = None   
