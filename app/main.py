from fastapi import FastAPI
from app.database import create_db_and_tables
from app import auth 

from app.routes import router as auth_router  # Your auth routes
from app.projects import router as projects_router 

app = FastAPI()
app.include_router(auth.router)


app.include_router(projects_router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"msg": "Welcome to FastAPI JWT Auth"}
