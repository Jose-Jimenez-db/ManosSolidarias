from scr.model.recurso_alimenticio import RecursoAlimenticio
from scr.model.entrega_alimentaria import EntregaAlimentaria

#---------------------------------------------------------------------------------------------

class ServicioEntrega:
    """Capa de lógica de negocio para entregas alimentarias."""

#---------------------------------------------------------------------------------------------

    def __init__(self, repositorio_entregas, repositorio_beneficiarios,
                 repositorio_recursos):
        """Inicializa el servicio con los repositorios necesarios para entregas."""
        self.repositorio_entregas = repositorio_entregas
        self.repositorio_beneficiarios = repositorio_beneficiarios
        self.repositorio_recursos = repositorio_recursos

#---------------------------------------------------------------------------------------------

    def registrar_entrega(self, codigo_entrega: str, identificacion_beneficiario: str,
                          codigo_recurso: str, cantidad_entregada, fecha: str,
                          responsable_entrega: str):
        """Registra una entrega alimentaria, descuenta inventario y calcula el valor económico."""
        if not codigo_entrega.strip():
            raise ValueError("El código de entrega no puede estar vacío...")

        datos_entrega = self.repositorio_entregas.buscar_por_campo(
            "codigo_entrega",
            codigo_entrega
        )

        if datos_entrega is not None:
            raise ValueError("Ya existe una entrega registrada con ese código...")

        datos_beneficiario = self.repositorio_beneficiarios.buscar_por_campo(
            "identificacion",
            identificacion_beneficiario
        )

        if datos_beneficiario is None:
            raise ValueError("No se puede registrar la entrega porque el beneficiario no existe...")

        datos_recurso = self.repositorio_recursos.buscar_por_campo(
            "codigo_recurso",
            codigo_recurso
        )

        if datos_recurso is None:
            raise ValueError("No se puede registrar la entrega porque el recurso no existe...")

        recurso = RecursoAlimenticio.from_dict(datos_recurso)

        try:
            cantidad_entregada = int(cantidad_entregada)
        except ValueError:
            raise ValueError("La cantidad entregada debe ser un número entero válido...")

        if cantidad_entregada <= 0:
            raise ValueError("La cantidad entregada debe ser mayor que cero...")

        if cantidad_entregada > recurso.cantidad_disponible:
            raise ValueError("No hay suficiente inventario disponible para realizar la entrega...")

        if not fecha.strip():
            raise ValueError("La fecha no puede estar vacía...")

        if not responsable_entrega.strip():
            raise ValueError("El responsable de entrega no puede estar vacío...")

        valor_economico = cantidad_entregada * recurso.costo_unitario

        entrega = EntregaAlimentaria(
            codigo_entrega,
            identificacion_beneficiario,
            codigo_recurso,
            cantidad_entregada,
            fecha,
            responsable_entrega,
            valor_economico
        )

        recurso.cantidad_disponible = recurso.cantidad_disponible - cantidad_entregada

        self.repositorio_recursos.actualizar(
            "codigo_recurso",
            codigo_recurso,
            recurso.to_dict()
        )

        self.repositorio_entregas.agregar(entrega.to_dict())

#---------------------------------------------------------------------------------------------

    def consultar_entregas(self):
        """Retorna todas las entregas alimentarias registradas."""
        resultado = []

        for datos_entrega in self.repositorio_entregas.cargar_todos():
            resultado.append(EntregaAlimentaria.from_dict(datos_entrega))

        return resultado

#---------------------------------------------------------------------------------------------

    def listar_entregas_por_beneficiario(self, identificacion_beneficiario: str):
        """Lista las entregas asociadas a un beneficiario específico."""
        resultado = []

        for datos_entrega in self.repositorio_entregas.cargar_todos():
            entrega = EntregaAlimentaria.from_dict(datos_entrega)

            if entrega.identificacion_beneficiario == identificacion_beneficiario:
                resultado.append(entrega)

        return resultado

#---------------------------------------------------------------------------------------------

    def listar_entregas_por_fecha(self, fecha: str):
        """Lista las entregas registradas en una fecha específica."""
        resultado = []

        for datos_entrega in self.repositorio_entregas.cargar_todos():
            entrega = EntregaAlimentaria.from_dict(datos_entrega)

            if entrega.fecha == fecha:
                resultado.append(entrega)

        return resultado

#---------------------------------------------------------------------------------------------

    def historial_entregas(self):
        """Retorna el historial completo de entregas alimentarias."""
        return self.consultar_entregas()

#---------------------------------------------------------------------------------------------