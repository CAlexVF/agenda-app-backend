# app/services/negocio_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status # <-- Importamos para manejar errores
from app.models.negocio import Negocio
from app.models.servicio import Servicio
from app.schemas.servicio import ServicioCreate

def obtener_lista_negocios(db: Session):
    return db.query(Negocio).all()

def crear_servicio_en_negocio(db: Session, servicio_data: ServicioCreate, negocio_id: int):
    # --- EL ESCUDO (Validación de Precondición) ---
    # 1. Buscamos si el negocio existe
    negocio_existente = db.query(Negocio).filter(Negocio.ID_Negocio == negocio_id).first()
    
    # 2. Si no existe, lanzamos un error 404 de inmediato
    if not negocio_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: No se encontró el negocio con ID {negocio_id}. No se puede agregar el servicio."
        )

    # 3. Si llegamos aquí, es porque el negocio sí existe. Procedemos a crear:
    nuevo_servicio = Servicio(
        ID_Negocio=negocio_id,
        Nombre_Servicio=servicio_data.nombre_servicio,
        Duracion_Minutos=servicio_data.duracion_minutos,
        Precio=servicio_data.precio
    )
    db.add(nuevo_servicio)
    db.commit()
    db.refresh(nuevo_servicio)
    return nuevo_servicio