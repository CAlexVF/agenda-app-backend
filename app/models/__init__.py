# app/models/__init__.py
from .negocio import Negocio
from .servicio import Servicio
from .usuario import Usuario

# Esto hace que cuando alguien importe "models", 
# automáticamente se registren ambas clases en SQLAlchemy.