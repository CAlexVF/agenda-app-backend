# app/models/negocio.py
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship # <-- Asegúrate de tener esta línea
from app.database import Base

class Negocio(Base):
    __tablename__ = "Negocios"

    ID_Negocio = Column(Integer, primary_key=True, index=True)
    ID_Dueño = Column(Integer)
    Nombre_Negocio = Column(String(100), nullable=False)
    Categoria = Column(String(50), nullable=False)
    Descripcion = Column(Text)
    Direccion = Column(String(255), nullable=False)
    Es_Recomendado = Column(Boolean, default=False)

    # Nueva línea para conectar con Servicios
    servicios = relationship("Servicio", back_populates="negocio", cascade="all, delete-orphan")