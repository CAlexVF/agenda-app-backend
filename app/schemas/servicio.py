# app/schemas/servicio.py
from pydantic import BaseModel, Field

class ServicioCreate(BaseModel):
    # Usamos Field para agregar reglas de calidad/validación
    nombre_servicio: str = Field(..., min_length=3, max_length=100)
    duracion_minutos: int = Field(..., gt=0) # Debe ser mayor a 0
    precio: float = Field(..., ge=0) # Debe ser mayor o igual a 0

    class Config:
        from_attributes = True