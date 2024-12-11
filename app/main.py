from fastapi import FastAPI
from app.routers.user import user_router
from app.db.database_config import create_db_and_tables
import uvicorn
# 

app = FastAPI(title="CSTAD Fast API with CI/CD",
        version="1.0.0", 
        description="This is a fast api application that implemented for testing with CI/CD")
# file handler for file media types
# added router

app.include_router(user_router, tags=["User"])

# when the application is started up then create tables
@app.on_event("startup")
async def startup():
    await create_db_and_tables()

@app.get("/", tags=["Home"])
async def root():
    return "Hello World!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)