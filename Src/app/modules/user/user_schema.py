from pydantic import BaseModel, EmailStr

# ----------- Request DTO ----------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# ----------- Response DTO ----------
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True  
