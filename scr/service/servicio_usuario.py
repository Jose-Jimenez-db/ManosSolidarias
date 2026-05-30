from scr.model.usuario import Usuario

#---------------------------------------------------------------------------------------------

class ServicioUsuario:
    """Capa de lógica de negocio para usuarios e inicio de sesión."""

#---------------------------------------------------------------------------------------------

    def __init__(self, repositorio_usuarios):
        """Inicializa el servicio con el repositorio de usuarios."""
        self.repositorio_usuarios = repositorio_usuarios

#---------------------------------------------------------------------------------------------

    def validar_inicio_sesion(self, usuario: str, contrasena: str):
        """Valida las credenciales de un usuario para permitir el acceso al sistema."""
        if not usuario.strip():
            raise ValueError("El usuario no puede estar vacío...")

        if not contrasena.strip():
            raise ValueError("La contraseña no puede estar vacía...")

        datos_usuario = self.repositorio_usuarios.buscar_por_campo("usuario", usuario)

        if datos_usuario is None:
            raise ValueError("El usuario ingresado no existe...")

        usuario_encontrado = Usuario.from_dict(datos_usuario)

        if usuario_encontrado.contrasena != contrasena:
            raise ValueError("La contraseña ingresada es incorrecta...")

        return True

#---------------------------------------------------------------------------------------------

    def registrar_usuario(self, usuario: str, contrasena: str):
        """Registra un usuario nuevo para el inicio de sesión."""
        if not usuario.strip():
            raise ValueError("El usuario no puede estar vacío...")

        if not contrasena.strip():
            raise ValueError("La contraseña no puede estar vacía...")

        datos_usuario = self.repositorio_usuarios.buscar_por_campo("usuario", usuario)

        if datos_usuario is not None:
            raise ValueError("Ya existe un usuario registrado con ese nombre...")

        nuevo_usuario = Usuario(usuario, contrasena)

        self.repositorio_usuarios.agregar(nuevo_usuario.to_dict())

#---------------------------------------------------------------------------------------------