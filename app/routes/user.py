
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users"
)

# For Users:


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut,
    tags=["Users"]
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hash password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Email already exists.")
    return new_user


@router.get(
    path="/{id}",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut,
    tags=["Users"]
)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with ID: {id} does not exist.")

    return user
