from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import SQLModel, Field, Session, select
from typing import Optional, List
from app.database import get_session
from app.auth import get_current_user
from app.models import User  # Assuming User model has a 'role' field
from app.models import Project

router = APIRouter()

# Define the Project model
#class Project(SQLModel, table=True):
    #id: Optional[int] = Field(default=None, primary_key=True)
    #name: str
    #description: str

class ProjectCreate(SQLModel):
    name: str
    description: str

# GET all projects (accessible to all logged-in users)
@router.get("/projects", response_model=List[Project])
def read_projects(session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    projects = session.exec(select(Project)).all()
    return projects

# POST project (admin only)
@router.post("/projects", response_model=Project)
def create_project(project: ProjectCreate, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create projects")
    new_project = Project(**project.dict())
    session.add(new_project)
    session.commit()
    session.refresh(new_project)
    return new_project

# PUT project (admin only)
@router.put("/projects/{project_id}", response_model=Project)
def update_project(project_id: int, project: ProjectCreate, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can update projects")
    existing = session.get(Project, project_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Project not found")
    existing.name = project.name
    existing.description = project.description
    session.add(existing)
    session.commit()
    session.refresh(existing)
    return existing

# DELETE project (admin only)
@router.delete("/projects/{project_id}", status_code=204)
def delete_project(project_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete projects")
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    session.delete(project)
    session.commit()
    return
