class EntregaAlimentaria:
    def __init__(self, codigo_entrega: str, identificacion_beneficiario: str,
                 codigo_recurso: str, cantidad_entregada: int,
                 fecha: str, responsable_entrega: str, valor_economico: float):
        self.codigo_entrega = codigo_entrega
        self.identificacion_beneficiario = identificacion_beneficiario
        self.codigo_recurso = codigo_recurso
        self.cantidad_entregada = cantidad_entregada
        self.fecha = fecha
        self.responsable_entrega = responsable_entrega
        self.valor_economico = valor_economico

    def to_dict(self) -> dict:
        return {
            "codigo_entrega": self.codigo_entrega,
            "identificacion_beneficiario": self.identificacion_beneficiario,
            "codigo_recurso": self.codigo_recurso,
            "cantidad_entregada": self.cantidad_entregada,
            "fecha": self.fecha,
            "responsable_entrega": self.responsable_entrega,
            "valor_economico": self.valor_economico
        }

    @classmethod
    def from_dict(cls, datos: dict) -> 'EntregaAlimentaria':
        return cls(
            datos["codigo_entrega"],
            datos["identificacion_beneficiario"],
            datos["codigo_recurso"],
            datos["cantidad_entregada"],
            datos["fecha"],
            datos["responsable_entrega"],
            datos["valor_economico"]
        )

    def __str__(self) -> str:
        return (f"Entrega: {self.codigo_entrega} | "
                f"Beneficiario: {self.identificacion_beneficiario} | "
                f"Recurso: {self.codigo_recurso} | "
                f"Cantidad: {self.cantidad_entregada} | "
                f"Fecha: {self.fecha} | "
                f"Responsable: {self.responsable_entrega} | "
                f"Valor: {self.valor_economico}")