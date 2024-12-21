from fastapi import FastAPI, HTTPException
from models import Ingredient
from routes import router
from recipes_router import rcp_router

# Initialize FastAPI app
app = FastAPI()

app.include_router(router)
app.include_router(rcp_router)