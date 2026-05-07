from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from models import user, task, comment
from routers.user import router as user_router

app = FastAPI()

# Include routers
app.include_router(user_router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    print("Server is starting...")
    
    # WARNING: This will drop all existing tables and recreate them
    # Uncomment the next two lines to reset database (will lose all data)
    # Base.metadata.drop_all(bind=engine)
    # print("Existing tables dropped!")
    
    # Create all database tables
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

@app.on_event("shutdown")
async def shutdown():
    print("Server is shutting down...")
