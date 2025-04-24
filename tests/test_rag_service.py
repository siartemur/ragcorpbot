from app.services.rag_service import ask_question

def test_rag_answer_generation():
    question = "Which languages are listed in the CV?"
    answer = ask_question(question)
    assert isinstance(answer, str)
    assert len(answer) > 0
