from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from . import models
# from .config import settings
# from .database import engine
# from .routers import auth, posts, users

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(posts.router)
# app.include_router(users.router)
# app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World!!!!!!!"}