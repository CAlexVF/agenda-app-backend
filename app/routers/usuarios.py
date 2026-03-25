# app/routers/usuarios.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.usuario_service import crear_nuevo_usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, UsuarioLogin, Token
from app.services.usuario_service import crear_nuevo_usuario, autenticar_usuario
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/api/usuarios", tags=["Usuarios"])

@router.post("/registro", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Llamamos al servicio que ya tiene la lógica de hashing y validación
    return crear_nuevo_usuario(db, usuario)

@router.post("/login", response_model=Token)
def login(
    login_data: OAuth2PasswordRequestForm = Depends(), # <-- Cambia UsuarioLogin por esto
    db: Session = Depends(get_db)
):
    # OAuth2PasswordRequestForm usa .username en lugar de .email
    # Así que pasamos los datos manualmente al servicio
    from app.schemas.usuario import UsuarioLogin
    data_para_servicio = UsuarioLogin(email=login_data.username, password=login_data.password)
    
    return autenticar_usuario(db, data_para_servicio)