# app/routers/negocios.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.negocio_service import obtener_lista_negocios

router = APIRouter(prefix="/api/negocios", tags=["Negocios"])

# Usamos "Depends(get_db)" para inyectar la conexión a la BD de forma segura
@router.get("/")
def listar_negocios(db: Session = Depends(get_db)):
    lista = obtener_lista_negocios(db)
    return {"mensaje": "Operación exitosa", "datos": lista}