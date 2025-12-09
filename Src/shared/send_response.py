from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

def send_response(message: str, data=None):
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": message,
            "data": jsonable_encoder(data)
        }
    )
