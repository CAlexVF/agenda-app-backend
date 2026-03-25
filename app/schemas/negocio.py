# app/schemas/negocio.py
from pydantic import BaseModel
from typing import List, Optional

class ServicioSchema(BaseModel):
    ID_Servicio: int
    Nombre_Servicio: str
    Duracion_Minutos: int
    Precio: float

    class Config:
        from_attributes = True

class NegocioConServicios(BaseModel):
    ID_Negocio: int
    Nombre_Negocio: str
    Categoria: str
    servicios: List[ServicioSchema] = []

    class Config:
        from_attributes = True