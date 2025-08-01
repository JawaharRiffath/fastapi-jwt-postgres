from sqlmodel import Session, select
from app import models
from app.utils import get_password_hash

from sqlmodel import Session
from app.models import User

#def get_user_by_username(db: Session, username: str) -> User | None:
    #return db.query(User).filter(User.username == username).first()

# Create new user
def create_user(username: str, password: str, role: str, session: Session):
    hashed_password = get_password_hash(password)
    user = models.User(username=username, hashed_password=hashed_password, role=role)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user_by_username(session: Session, username: str) -> User | None:
    statement = select(User).where(User.username == username)
    return session.exec(statement).first()