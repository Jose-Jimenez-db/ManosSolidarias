from scr.model.beneficiario import Beneficiario

#---------------------------------------------------------------------------------------------

class ServicioBeneficiario:
    """Capa de lógica de negocio para beneficiarios."""

#---------------------------------------------------------------------------------------------

    def __init__(self, repositorio_beneficiarios):
        """Inicializa el servicio con el repositorio de beneficiarios."""
        self.repositorio_beneficiarios = repositorio_beneficiarios

#---------------------------------------------------------------------------------------------

    def registrar_beneficiario(self, identificacion: str, nombre_completo: str,
                               comunidad: str, integrantes_hogar, prioridad_social: str):
        """Registra un nuevo beneficiario validando las reglas de negocio."""
        if not identificacion.strip():
            raise ValueError("La identificación no puede estar vacía...")

        datos_beneficiario = self.repositorio_beneficiarios.buscar_por_campo(
            "identificacion",
            identificacion
        )

        if datos_beneficiario is not None:
            raise ValueError("Ya existe un beneficiario registrado con esa identificación...")

        if not nombre_completo.strip():
            raise ValueError("El nombre completo no puede estar vacío...")

        if not comunidad.strip():
            raise ValueError("La comunidad no puede estar vacía...")

        try:
            integrantes_hogar = int(integrantes_hogar)
        except ValueError:
            raise ValueError("La cantidad de integrantes debe ser un número entero válido...")

        if integrantes_hogar <= 0:
            raise ValueError("La cantidad de integrantes debe ser mayor que cero...")

        if prioridad_social not in ["Alta", "Media", "Baja"]:
            raise ValueError("La prioridad social debe ser Alta, Media o Baja...")

        beneficiario = Beneficiario(
            identificacion,
            nombre_completo,
            comunidad,
            integrantes_hogar,
            prioridad_social
        )

        self.repositorio_beneficiarios.agregar(beneficiario.to_dict())

#---------------------------------------------------------------------------------------------

    def consultar_beneficiarios(self):
        """Retorna todos los beneficiarios registrados."""
        resultado = []

        for datos_beneficiario in self.repositorio_beneficiarios.cargar_todos():
            resultado.append(Beneficiario.from_dict(datos_beneficiario))

        return resultado

#---------------------------------------------------------------------------------------------

    def buscar_beneficiario(self, identificacion: str):
        """Busca un beneficiario por identificación."""
        datos_beneficiario = self.repositorio_beneficiarios.buscar_por_campo(
            "identificacion",
            identificacion
        )

        if datos_beneficiario is None:
            return None

        return Beneficiario.from_dict(datos_beneficiario)

#---------------------------------------------------------------------------------------------

    def eliminar_beneficiario(self, identificacion: str):
        """Elimina un beneficiario por identificación."""
        return self.repositorio_beneficiarios.eliminar_por_campo(
            "identificacion",
            identificacion
        )

#---------------------------------------------------------------------------------------------

    def listar_beneficiarios_por_comunidad(self, comunidad: str):
        """Lista los beneficiarios pertenecientes a una comunidad específica."""
        resultado = []

        for datos_beneficiario in self.repositorio_beneficiarios.cargar_todos():
            beneficiario = Beneficiario.from_dict(datos_beneficiario)

            if beneficiario.comunidad == comunidad:
                resultado.append(beneficiario)

        return resultado

#---------------------------------------------------------------------------------------------