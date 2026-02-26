from app.services.negocio_service import obtener_lista_negocios

def test_obtener_lista_negocios_vacia():
    # Simulamos pedir la lista de negocios cuando el sistema está nuevo
    resultado = obtener_lista_negocios()
    
    # Esperamos que nos devuelva una lista vacía
    assert resultado == []