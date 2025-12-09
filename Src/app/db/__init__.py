from sqlalchemy.ext.asyncio import AsyncEngine
from app.db.database import Base
# OR:
# from app.modules.user.user_model import Base  # if Base is in model file

async def init_db(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
