from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.database import get_session
from app import schemas, crud, auth
from app.schemas import UserCreate, UserRead  # Make sure both are imported

router = APIRouter()

@router.post("/register", response_model=schemas.UserRead)
def signup(user: schemas.UserCreate, session: Session = Depends(get_session)):
    db_user = crud.get_user_by_username(user.username, session)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(user.username, user.password, user.role, session)


@router.post("/login")
def login(user: schemas.UserCreate, session: Session = Depends(get_session)):
    db_user = crud.get_user_by_username(user.username, session)
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = auth.create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
