from openai import OpenAI
from app.config.settings import OPENAI_API_KEY

def get_openai_client() -> OpenAI:
    """
    Returns a new OpenAI client instance each time it is called.
    This avoids crashing the app during module import if key is missing.
    """
    if not OPENAI_API_KEY:
        raise ValueError("❌ OPENAI_API_KEY is not defined in the .env file.")
    return OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """
    Generates a response from GPT for a given prompt.
    """
    try:
        client = get_openai_client()
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an assistant bot that provides access to corporate documents."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            timeout=20
        )
        return response.choices[0].message.content.strip() if response.choices else "No response received."
    except Exception as e:
        print(f"[ERROR - GPT]: {str(e)}")
        return "⚠️ Failed to get GPT response. (debug)"
