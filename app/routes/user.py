
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    # prefix="/users",
)

# For Users:


@router.post(
    path="/users",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut,
    tags=["Users"],
    summary="Create a new user"
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    # Create User
    You can create a new user.
    # Parameters
    - email: this will be your username,
    - password: password to access to plataform.
    # Return
    - UserId confirms that user was created well.
    """
    # hash password - user.password
    print(user)
    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get(
    path="/{id}",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut,
    tags=["Users"],
    summary="Show a user by Id"
)
def get_user(id: int, db: Session = Depends(get_db)):
    """
    # Show User
    Return a basic information of users that was been created.
    # Parameters
    - Id: it's the Id asignend to a user when was created.
    # Return
    - Id as user id. Email as username and created_at with data when user was created.
    """
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with ID: {id} does not exist.")

    return user
