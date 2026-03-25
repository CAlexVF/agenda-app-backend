# app/services/usuario_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.usuario import Usuario
from app.core.security import obtener_password_hash
from app.core.security import obtener_password_hash, verificar_password, crear_token_acceso
from app.schemas.usuario import UsuarioCreate, UsuarioLogin

def crear_nuevo_usuario(db: Session, usuario_data: UsuarioCreate):
    # 1. Verificar si el email ya está registrado (Regla de Calidad)
    email_existe = db.query(Usuario).filter(Usuario.Email == usuario_data.email).first()
    if email_existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado."
        )

    # 2. Hashear la contraseña (Seguridad)
    print(f"DEBUG: Texto enviado al hash: '{usuario_data.password}' | Largo: {len(usuario_data.password)}")
    password_segura = obtener_password_hash(usuario_data.password)

    # 3. Crear la instancia del modelo
    nuevo_usuario = Usuario(
        Nombre_Completo=usuario_data.nombre_completo,
        Email=usuario_data.email,
        Password_Hash=password_segura,
        Rol=usuario_data.rol
    )

    # 4. Guardar en la base de datos
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def autenticar_usuario(db: Session, login_data: UsuarioLogin):
    # 1. Buscar al usuario por email
    usuario = db.query(Usuario).filter(Usuario.Email == login_data.email).first()
    
    # 2. Si no existe o la contraseña no coincide, lanzamos error 401 (No autorizado)
    if not usuario or not verificar_password(login_data.password, usuario.Password_Hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Si todo está bien, generamos su Token
    token_data = {"sub": usuario.Email, "rol": usuario.Rol}
    token = crear_token_acceso(data=token_data)
    
    return {"access_token": token, "token_type": "bearer"}