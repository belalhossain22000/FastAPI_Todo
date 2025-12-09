from fastapi import Request, HTTPException, Depends
from pydantic import BaseModel

def validate_request(schema: type[BaseModel]):
    async def dependency(request: Request):
        try:
            body = await request.json()
            return schema(**body)
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))
    return Depends(dependency)
