from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.modules.user.user_schema import UserCreate, UserResponse
from app.modules.user.user_controller import UserController
from app.middlewares.validateRequest import validate_request

router = APIRouter()
controller = UserController()

@router.post("/", response_model=UserResponse)
async def create_user(payload: UserCreate = validate_request(UserCreate), db: AsyncSession = Depends(get_db)):
    return await controller.create_user(db, payload)

@router.get("/", response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    return await controller.get_all_users(db)
