# app/models/servicio.py
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database import Base

class Servicio(Base):
    __tablename__ = "Servicios"

    ID_Servicio = Column(Integer, primary_key=True, index=True)
    ID_Negocio = Column(Integer, ForeignKey("Negocios.ID_Negocio"))
    Nombre_Servicio = Column(String(100), nullable=False)
    Duracion_Minutos = Column(Integer, nullable=False)
    Precio = Column(Numeric(10, 2), nullable=False)

    # Relación: Muchos servicios pertenecen a un Negocio
    negocio = relationship("Negocio", back_populates="servicios")