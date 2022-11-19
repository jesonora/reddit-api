"""The main APIRouter is defined to include all the sub routers from each module inside the API folder"""
from fastapi import APIRouter
from .base import base_router

"""
FastAPI has a system of APIRouters. These can be considered to be mini FastAPI apps that are part of the bigger app.
It means one can break bigger app routes into small units of APIRouters and mount individual APIRouters in the main app.
These APIRouters can have separate prefixes to the path operations, tags, dependencies and responses.
"""
api_router = APIRouter()
api_router.include_router(base_router, tags=["base"])
