class RecursoAlimenticio:
    def __init__(self, codigo_recurso: str, nombre: str, categoria: str,
                 cantidad_disponible: int, costo_unitario: float):
        self.codigo_recurso = codigo_recurso
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad_disponible = cantidad_disponible
        self.costo_unitario = costo_unitario

    def to_dict(self) -> dict:
        return {
            "codigo_recurso": self.codigo_recurso,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "cantidad_disponible": self.cantidad_disponible,
            "costo_unitario": self.costo_unitario
        }

    @classmethod
    def from_dict(cls, datos: dict) -> 'RecursoAlimenticio':
        return cls(
            datos["codigo_recurso"],
            datos["nombre"],
            datos["categoria"],
            datos["cantidad_disponible"],
            datos["costo_unitario"]
        )

    def __str__(self) -> str:
        return (f"Recurso: {self.nombre} | "
                f"Código: {self.codigo_recurso} | "
                f"Categoría: {self.categoria} | "
                f"Disponible: {self.cantidad_disponible} | "
                f"Costo: {self.costo_unitario}")