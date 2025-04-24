from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str  # ileride hash'e çevrilebilir
    role: str  # "admin" veya "user"
