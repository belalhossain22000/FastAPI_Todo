from fastapi import FastAPI
from app.routes.index import api_router
from app.db.database import Base, engine

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("🔥 Tables created successfully!")

app.include_router(api_router,prefix="/api/v1")
