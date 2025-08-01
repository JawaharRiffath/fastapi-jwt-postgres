from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from .models import User
from app.database import get_session
from .auth import SECRET_KEY, ALGORITHM
from sqlmodel import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_admin_user(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return current_user

