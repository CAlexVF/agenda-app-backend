# app/routers/negocios.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.security import obtener_usuario_actual

from app.database import get_db
# AGREGAMOS crear_servicio_en_negocio al import de abajo:
from app.services.negocio_service import obtener_lista_negocios, crear_servicio_en_negocio
from app.schemas.negocio import NegocioConServicios
from app.schemas.servicio import ServicioCreate

router = APIRouter(prefix="/api/negocios", tags=["Negocios"])

@router.get("/", response_model=List[NegocioConServicios])
def listar_negocios(db: Session = Depends(get_db)):
    lista = obtener_lista_negocios(db)
    return lista

@router.post("/{negocio_id}/servicios")
def agregar_servicio(
    negocio_id: int, 
    servicio: ServicioCreate, 
    db: Session = Depends(get_db),
    usuario_email: str = Depends(obtener_usuario_actual) # <-- ¡EL GUARDIA!
):
    # Ahora esta ruta está protegida. Si no mandan token, FastAPI da error 401
    return crear_servicio_en_negocio(db, servicio, negocio_id)