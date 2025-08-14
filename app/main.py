from fastapi import FastAPI
from app.database.database import engine
from app.api.routes import router

app = FastAPI()

# Include the API routes
app.include_router(router)

# Create the database tables
@app.on_event("startup")
async def startup():
    import app.database.models  # Import models to create tables

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Address Book API!"}