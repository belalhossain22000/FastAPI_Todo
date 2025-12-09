from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.modules.user.user_model import User
from app.modules.user.user_schema import UserCreate, UserResponse
from errors.api_errors import ApiError
from helpers.jwtHelpers import hash_password


class UserService:

    async def create_user(self, db: AsyncSession, data: UserCreate):
        # Check if email already exists
        query = select(User).where(User.email == data.email)
        result = await db.execute(query)
        existing = result.scalar_one_or_none()

        if existing:
            raise ApiError(400, "Email already exists")

        # Hash password
        hashed_pass = hash_password(data.password)

        user = User(
            name=data.name,
            email=data.email,
            password=hashed_pass,
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

        # Convert SQLAlchemy User model → Pydantic UserResponse
        return UserResponse.model_validate(user)

    async def get_users(self, db: AsyncSession):
        query = select(User)
        result = await db.execute(query)
        users = result.scalars().all()

        # Convert list of ORM users → list of Pydantic models
        return [UserResponse.model_validate(u) for u in users]
