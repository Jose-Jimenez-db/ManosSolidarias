from scr.model.beneficiario import Beneficiario
from scr.model.recurso_alimenticio import RecursoAlimenticio
from scr.model.entrega_alimentaria import EntregaAlimentaria

#---------------------------------------------------------------------------------------------

class ServicioReporte:
    """Capa de lógica de negocio para reportes del sistema."""

#---------------------------------------------------------------------------------------------

    def __init__(self, repositorio_beneficiarios, repositorio_recursos,
                 repositorio_entregas):
        """Inicializa el servicio con los repositorios necesarios para reportes."""
        self.repositorio_beneficiarios = repositorio_beneficiarios
        self.repositorio_recursos = repositorio_recursos
        self.repositorio_entregas = repositorio_entregas

#---------------------------------------------------------------------------------------------

    def reporte_beneficiarios_por_comunidad(self):
        """Retorna una lista de tuplas con la comunidad y la cantidad de beneficiarios."""
        conteo = {}

        for datos_beneficiario in self.repositorio_beneficiarios.cargar_todos():
            beneficiario = Beneficiario.from_dict(datos_beneficiario)
            comunidad = beneficiario.comunidad
            conteo[comunidad] = conteo.get(comunidad, 0) + 1

        resultado = []

        for comunidad, cantidad in conteo.items():
            resultado.append((comunidad, cantidad))

        return resultado

#---------------------------------------------------------------------------------------------

    def reporte_recursos_inventario_bajo(self, limite):
        """Retorna una lista de tuplas con los recursos cuya cantidad disponible está por debajo del límite."""
        try:
            limite = int(limite)
        except ValueError:
            raise ValueError("El límite mínimo debe ser un número entero válido...")

        resultado = []

        for datos_recurso in self.repositorio_recursos.cargar_todos():
            recurso = RecursoAlimenticio.from_dict(datos_recurso)

            if recurso.cantidad_disponible < limite:
                resultado.append((
                    recurso.codigo_recurso,
                    recurso.nombre,
                    recurso.cantidad_disponible
                ))

        return resultado

#---------------------------------------------------------------------------------------------

    def reporte_recursos_mas_entregados(self):
        """Retorna una lista de tuplas con los recursos más entregados y su cantidad total entregada."""
        acumulado = {}

        for datos_entrega in self.repositorio_entregas.cargar_todos():
            entrega = EntregaAlimentaria.from_dict(datos_entrega)
            codigo_recurso = entrega.codigo_recurso
            acumulado[codigo_recurso] = (
                acumulado.get(codigo_recurso, 0) + entrega.cantidad_entregada
            )

        resultado = []

        for codigo_recurso, cantidad_total in acumulado.items():
            datos_recurso = self.repositorio_recursos.buscar_por_campo(
                "codigo_recurso",
                codigo_recurso
            )

            if datos_recurso is not None:
                recurso = RecursoAlimenticio.from_dict(datos_recurso)
                resultado.append((recurso.nombre, cantidad_total))

        resultado.sort(key=lambda dato: dato[1], reverse=True)

        return resultado

#---------------------------------------------------------------------------------------------

    def reporte_costo_total_ayuda_distribuida(self):
        """Retorna el costo total de toda la ayuda alimentaria distribuida."""
        total = 0

        for datos_entrega in self.repositorio_entregas.cargar_todos():
            entrega = EntregaAlimentaria.from_dict(datos_entrega)
            total = total + entrega.valor_economico

        return total

#---------------------------------------------------------------------------------------------