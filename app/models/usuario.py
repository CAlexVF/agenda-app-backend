# app/models/usuario.py
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class Usuario(Base):
    __tablename__ = "Usuarios"

    ID_Usuario = Column(Integer, primary_key=True, index=True)
    Nombre_Completo = Column(String(100), nullable=False)
    Email = Column(String(100), unique=True, index=True, nullable=False)
    Password_Hash = Column(String(255), nullable=False)
    Rol = Column(Enum('Cliente', 'Dueño'), nullable=False)
    Fecha_Registro = Column(TIMESTAMP, server_default=func.now())