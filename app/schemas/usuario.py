# app/schemas/usuario.py
from pydantic import BaseModel, EmailStr, Field

class UsuarioCreate(BaseModel):
    nombre_completo: str = Field(..., min_length=3)
    email: EmailStr # Esto valida automáticamente que sea un correo real
    password: str = Field(..., min_length=8)
    rol: str # 'Cliente' o 'Dueño'

class UsuarioResponse(BaseModel):
    ID_Usuario: int
    Nombre_Completo: str
    Email: str
    Rol: str

    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str