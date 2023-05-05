from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=["Authentication"])


@router.post(
    path="/login",
    response_model=schemas.Token,
    summary="To register with a user"
)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    """
    # Authentication
    If you want to post, update or delete a post you must need to be logged in.
    # Parameters
    - username: email that use for register.
    - password: password that you register.
    # Return
    - Return with a token "access_token" for authentication and type "token_type" as "bearer".
    """

    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")

    # create a token

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    # return token
    return {"access_token": access_token, "token_type": "bearer"}
