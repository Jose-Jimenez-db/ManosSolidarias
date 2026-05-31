class Beneficiario:
    """Representa un beneficiario del sistema."""

#---------------------------------------------------------------------------------------------

    def __init__(self, identificacion: str, nombre_completo: str, comunidad: str,
                 integrantes_hogar: int, prioridad_social: str):
        """Inicializa un beneficiario."""
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.comunidad = comunidad
        self.integrantes_hogar = integrantes_hogar
        self.prioridad_social = prioridad_social

#---------------------------------------------------------------------------------------------

    def to_dict(self) -> dict:
        """Convierte el beneficiario a diccionario."""
        return {
            "identificacion": self.identificacion,
            "nombre_completo": self.nombre_completo,
            "comunidad": self.comunidad,
            "integrantes_hogar": self.integrantes_hogar,
            "prioridad_social": self.prioridad_social
        }

#---------------------------------------------------------------------------------------------

    @classmethod
    def from_dict(cls, datos: dict) -> 'Beneficiario':
        """Crea un beneficiario desde un diccionario."""
        return cls(
            datos["identificacion"],
            datos["nombre_completo"],
            datos["comunidad"],
            datos["integrantes_hogar"],
            datos["prioridad_social"]
        )

#---------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        """Devuelve una representación en texto del beneficiario."""
        return (f"Beneficiario: {self.nombre_completo} | "
                f"ID: {self.identificacion} | "
                f"Comunidad: {self.comunidad} | "
                f"Integrantes: {self.integrantes_hogar} | "
                f"Prioridad: {self.prioridad_social}")

#---------------------------------------------------------------------------------------------