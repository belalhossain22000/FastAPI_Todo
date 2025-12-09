from fastapi import APIRouter

from app.modules.user.user_route import router as user_router


api_router = APIRouter()

module_routes = [
    {
        "path": "/users", 
        "router": user_router, 
        "tags": ["Users"]
    },
]

for r in module_routes:
    api_router.include_router(r["router"], prefix=r["path"], tags=r["tags"])
