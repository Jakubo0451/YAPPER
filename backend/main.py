from fastapi import FastAPI, Depends
import uvicorn
from database import engine, Base
from routers import users, tweets

Base.metadata.create_all(bind=engine)

app = FastAPI()

# include users router
app.include_router(users.router)
app.include_router(tweets.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)