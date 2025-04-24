from fastapi import APIRouter, Request, Response, Form, HTTPException
from app.config.settings import ADMIN_USERNAME, ADMIN_PASSWORD

router = APIRouter()

@router.post("/login")
async def login(response: Response, username: str = Form(...), password: str = Form(...)):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        response.set_cookie(key="role", value="admin", httponly=True)
        print(f"[LOGIN] Admin login successful: {username}")
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("role")
    return {"message": "Logged out successfully"}
