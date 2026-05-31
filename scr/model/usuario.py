class Usuario:
    """Representa un usuario del sistema."""

#---------------------------------------------------------------------------------------------

    def __init__(self, usuario: str, contrasena: str):
        """Inicializa un usuario."""
        self.usuario = usuario
        self.contrasena = contrasena

#---------------------------------------------------------------------------------------------

    def to_dict(self) -> dict:
        """Convierte el usuario a diccionario."""
        return {
            "usuario": self.usuario,
            "contrasena": self.contrasena
        }

#---------------------------------------------------------------------------------------------

    @classmethod
    def from_dict(cls, datos: dict) -> 'Usuario':
        """Crea un usuario desde un diccionario."""
        return cls(
            datos["usuario"],
            datos["contrasena"]
        )

#---------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        """Devuelve una representación en texto del usuario."""
        return f"Usuario: {self.usuario}"

#---------------------------------------------------------------------------------------------