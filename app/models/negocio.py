# app/models/negocio.py
from sqlalchemy import Column, Integer, String, Boolean, Text
from app.database import Base

class Negocio(Base):
    __tablename__ = "Negocios" # Debe coincidir EXACTAMENTE con el nombre en MySQL

    ID_Negocio = Column(Integer, primary_key=True, index=True)
    ID_Dueño = Column(Integer) # Por ahora lo dejamos como un entero simple
    Nombre_Negocio = Column(String(100), nullable=False)
    Categoria = Column(String(50), nullable=False)
    Descripcion = Column(Text)
    Direccion = Column(String(255), nullable=False)
    Es_Recomendado = Column(Boolean, default=False)