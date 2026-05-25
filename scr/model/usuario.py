class Usuario:
    def __init__(self, usuario: str, contrasena: str):
        self.usuario = usuario
        self.contrasena = contrasena

    def to_dict(self) -> dict:
        return {
            "usuario": self.usuario,
            "contrasena": self.contrasena
        }

    @classmethod
    def from_dict(cls, datos: dict) -> 'Usuario':
        return cls(
            datos["usuario"],
            datos["contrasena"]
        )

    def __str__(self) -> str:
        return f"Usuario: {self.usuario}"