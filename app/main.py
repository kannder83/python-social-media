
from fastapi import FastAPI, status
from .database import engine
from .routes import user, post, auth, vote
from fastapi.middleware.cors import CORSMiddleware


app: FastAPI = FastAPI()

# Configuration CORS:

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get(
    path="/",
    tags=["Test"],
    status_code=status.HTTP_200_OK,
    summary="Response if server is working well"
)
def root():
    """
    # Test
    Response if server is up an working!
    """
    return {"message": "Hello, API is working!"}
