from app.services.embedding_service import get_embedding

def test_embedding_output():
    text = "Enterprise artificial intelligence solutions"
    vector = get_embedding(text)
    assert isinstance(vector, list)
    assert len(vector) > 0
