from fastapi import Request, HTTPException

def verify_admin(request: Request):
    role = request.cookies.get("role")
    if role != "admin":
        raise HTTPException(status_code=403, detail="You do not have permission to perform this operation.")
