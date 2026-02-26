# app/main.py
from fastapi import FastAPI
from app.routers import negocios

# Inicializamos la aplicación
app = FastAPI(
    title="API de Agenda y Citas",
    description="Backend para el proyecto de Calidad de Software",
    version="0.1.0"
)

# Conectamos nuestro router de negocios a la app principal
app.include_router(negocios.router)

@app.get("/")
def raiz():
    return {"mensaje": "Bienvenido a la API de Agenda. Ve a /docs para ver la documentación."}