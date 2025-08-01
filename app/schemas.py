from pydantic import BaseModel

# Request body for user signup/login
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: str  # Add this


# DB response (if needed)
class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str

# Token Data schema for decoding JWT
class TokenData(BaseModel):
    username: str | None = None

class UserRead(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True
