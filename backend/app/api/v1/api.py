from fastapi import APIRouter
from app.api.v1.endpoints import properties, users, auth

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(properties.router, prefix="/properties", tags=["properties"])
api_router.include_router(users.router, prefix="/users", tags=["users"]) 