from dataclasses import dataclass

@dataclass
class DocumentChunk:
    content: str
    page_number: int
    chunk_index: int 
    source_file: str
