from scr.model.recurso_alimenticio import RecursoAlimenticio

#---------------------------------------------------------------------------------------------

class ServicioRecurso:
    """Capa de lógica de negocio para recursos alimenticios."""

#---------------------------------------------------------------------------------------------

    def __init__(self, repositorio_recursos):
        """Inicializa el servicio con el repositorio de recursos alimenticios."""
        self.repositorio_recursos = repositorio_recursos

#---------------------------------------------------------------------------------------------

    def registrar_recurso(self, codigo_recurso: str, nombre: str, categoria: str,
                          cantidad_disponible, costo_unitario):
        """Registra un nuevo recurso alimenticio validando las reglas de negocio."""
        if not codigo_recurso.strip():
            raise ValueError("El código del recurso no puede estar vacío...")

        datos_recurso = self.repositorio_recursos.buscar_por_campo(
            "codigo_recurso",
            codigo_recurso
        )

        if datos_recurso is not None:
            raise ValueError("Ya existe un recurso registrado con ese código...")

        if not nombre.strip():
            raise ValueError("El nombre del recurso no puede estar vacío...")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía...")

        try:
            cantidad_disponible = int(cantidad_disponible)
        except ValueError:
            raise ValueError("La cantidad disponible debe ser un número entero válido...")

        if cantidad_disponible < 0:
            raise ValueError("La cantidad disponible no puede ser negativa...")

        try:
            costo_unitario = float(costo_unitario)
        except ValueError:
            raise ValueError("El costo unitario debe ser un número válido...")

        if costo_unitario <= 0:
            raise ValueError("El costo unitario debe ser mayor que cero...")

        recurso = RecursoAlimenticio(
            codigo_recurso,
            nombre,
            categoria,
            cantidad_disponible,
            costo_unitario
        )

        self.repositorio_recursos.agregar(recurso.to_dict())

#---------------------------------------------------------------------------------------------

    def consultar_recursos(self):
        """Retorna todos los recursos alimenticios registrados."""
        resultado = []

        for datos_recurso in self.repositorio_recursos.cargar_todos():
            resultado.append(RecursoAlimenticio.from_dict(datos_recurso))

        return resultado

#---------------------------------------------------------------------------------------------

    def buscar_recurso(self, codigo_recurso: str):
        """Busca un recurso alimenticio por código."""
        datos_recurso = self.repositorio_recursos.buscar_por_campo(
            "codigo_recurso",
            codigo_recurso
        )

        if datos_recurso is None:
            return None

        return RecursoAlimenticio.from_dict(datos_recurso)

#---------------------------------------------------------------------------------------------

    def eliminar_recurso(self, codigo_recurso: str):
        """Elimina un recurso alimenticio por código."""

        if not codigo_recurso.strip():
            raise ValueError("El código del recurso no puede estar vacío...")

        datos_recurso = self.repositorio_recursos.buscar_por_campo(
            "codigo_recurso",
            codigo_recurso
        )

        if datos_recurso is None:
            raise ValueError("No existe un recurso registrado con ese código...")

        return self.repositorio_recursos.eliminar_por_campo(
            "codigo_recurso",
            codigo_recurso
        )

#---------------------------------------------------------------------------------------------

    def listar_recursos_por_categoria(self, categoria: str):
        """Lista los recursos alimenticios pertenecientes a una categoría específica."""
        resultado = []

        for datos_recurso in self.repositorio_recursos.cargar_todos():
            recurso = RecursoAlimenticio.from_dict(datos_recurso)

            if recurso.categoria == categoria:
                resultado.append(recurso)

        return resultado

#---------------------------------------------------------------------------------------------