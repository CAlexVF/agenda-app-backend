# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Aquí configuramos la ruta a tu MySQL local
# Formato: mysql+pymysql://USUARIO:CONTRASEÑA@SERVIDOR:PUERTO/BASE_DE_DATOS
# Sustituye "tu_contraseña" por la contraseña que usas en MySQL Workbench
URL_BASE_DATOS = "mysql+pymysql://root:root@localhost:3306/AgendaAppDB"

# El "motor" que maneja la conexión
engine = create_engine(URL_BASE_DATOS)

# La fábrica de sesiones (cada vez que hagamos una consulta, abrimos una sesión)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# La clase base de la cual heredarán nuestros modelos
Base = declarative_base()

# Esta función nos dará una conexión a la BD cada vez que alguien haga una petición web
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()