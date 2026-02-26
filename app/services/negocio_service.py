# app/services/negocio_service.py
from sqlalchemy.orm import Session
from app.models.negocio import Negocio

def obtener_lista_negocios(db: Session):
    # Esto equivale a un SELECT * FROM Negocios; pero al estilo Python
    negocios = db.query(Negocio).all()
    return negocios