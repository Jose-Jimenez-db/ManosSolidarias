from scr.model.beneficiario import Beneficiario
from scr.model.recurso_alimenticio import RecursoAlimenticio
from scr.model.entrega_alimentaria import EntregaAlimentaria
from scr.model.usuario import Usuario

#---------------------------------------------------------------------------------------------

class Servicio:
    """
    Capa de lógica de negocio del sistema Manos Solidarias.
    Se encarga de validar datos, coordinar repositorios y ejecutar procesos del sistema.
    """

#---------------------------------------------------------------------------------------------

    def __init__(self, repositorio_beneficiarios, repositorio_recursos,
                 repositorio_entregas, repositorio_usuarios):
        """Inicializa el servicio con los repositorios necesarios del sistema."""
        self.repositorio_beneficiarios = repositorio_beneficiarios
        self.repositorio_recursos = repositorio_recursos
        self.repositorio_entregas = repositorio_entregas
        self.repositorio_usuarios = repositorio_usuarios

#---------------------------------------------------------------------------------------------

    # USUARIOS:

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

    # BENEFICIARIOS:

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

    # RECURSOS ALIMENTICIOS:

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

    # ENTREGAS ALIMENTARIAS:

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

    # REPORTES:

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