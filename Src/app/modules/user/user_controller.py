from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.user.user_service import UserService
from app.modules.user.user_schema import UserCreate
from shared.send_response import send_response

user_service = UserService()

class UserController:

    async def create_user(self, db: AsyncSession, payload: UserCreate):
        user = await user_service.create_user(db, payload)
        return send_response("User created successfully", user)

    async def get_all_users(self, db: AsyncSession):
        users = await user_service.get_users(db)
        return send_response("Users fetched successfully", users)
