from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

import database
import schemas
import oauth2
from repository import blog
router = APIRouter(
    prefix="",
    tags=["Blogs"],
)


@router.get("/", response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_by_id(id: int, db: Session = Depends(database.get_db)):
    return blog.get_by_id(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    return blog.create(request, db, current_user)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_by_id(
    id: int,
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.update(id, request, db, current_user)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.delete(id, db, current_user)
