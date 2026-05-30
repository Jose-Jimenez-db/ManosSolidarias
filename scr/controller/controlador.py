class Controlador:
    """
    Controlador principal del sistema Manos Solidarias.
    Conecta la vista con las capas de servicio del sistema.
    """

#---------------------------------------------------------------------------------------------

    def __init__(self, servicio_usuario, servicio_beneficiario,
                 servicio_recurso, servicio_entrega, servicio_reporte):
        """Inicializa el controlador con los servicios principales del sistema."""
        self.servicio_usuario = servicio_usuario
        self.servicio_beneficiario = servicio_beneficiario
        self.servicio_recurso = servicio_recurso
        self.servicio_entrega = servicio_entrega
        self.servicio_reporte = servicio_reporte

#---------------------------------------------------------------------------------------------

    # USUARIOS:

    def validar_inicio_sesion(self, usuario, contrasena):
        """Solicita al servicio validar las credenciales de inicio de sesión."""
        return self.servicio_usuario.validar_inicio_sesion(usuario, contrasena)

#---------------------------------------------------------------------------------------------

    def registrar_usuario(self, usuario, contrasena):
        """Solicita al servicio registrar un nuevo usuario."""
        return self.servicio_usuario.registrar_usuario(usuario, contrasena)

#---------------------------------------------------------------------------------------------

    # BENEFICIARIOS:

    def registrar_beneficiario(self, identificacion, nombre_completo, comunidad,
                               integrantes_hogar, prioridad_social):
        """Solicita al servicio registrar un beneficiario."""
        return self.servicio_beneficiario.registrar_beneficiario(
            identificacion,
            nombre_completo,
            comunidad,
            integrantes_hogar,
            prioridad_social
        )

#---------------------------------------------------------------------------------------------

    def consultar_beneficiarios(self):
        """Solicita al servicio todos los beneficiarios registrados."""
        return self.servicio_beneficiario.consultar_beneficiarios()

#---------------------------------------------------------------------------------------------

    def buscar_beneficiario(self, identificacion):
        """Solicita al servicio buscar un beneficiario por identificación."""
        return self.servicio_beneficiario.buscar_beneficiario(identificacion)

#---------------------------------------------------------------------------------------------

    def eliminar_beneficiario(self, identificacion):
        """Solicita al servicio eliminar un beneficiario por identificación."""
        return self.servicio_beneficiario.eliminar_beneficiario(identificacion)

#---------------------------------------------------------------------------------------------

    def listar_beneficiarios_por_comunidad(self, comunidad):
        """Solicita al servicio listar beneficiarios por comunidad."""
        return self.servicio_beneficiario.listar_beneficiarios_por_comunidad(comunidad)

#---------------------------------------------------------------------------------------------

    # RECURSOS ALIMENTICIOS:

    def registrar_recurso(self, codigo_recurso, nombre, categoria,
                          cantidad_disponible, costo_unitario):
        """Solicita al servicio registrar un recurso alimenticio."""
        return self.servicio_recurso.registrar_recurso(
            codigo_recurso,
            nombre,
            categoria,
            cantidad_disponible,
            costo_unitario
        )

#---------------------------------------------------------------------------------------------

    def consultar_recursos(self):
        """Solicita al servicio todos los recursos alimenticios registrados."""
        return self.servicio_recurso.consultar_recursos()

#---------------------------------------------------------------------------------------------

    def buscar_recurso(self, codigo_recurso):
        """Solicita al servicio buscar un recurso alimenticio por código."""
        return self.servicio_recurso.buscar_recurso(codigo_recurso)

#---------------------------------------------------------------------------------------------

    def eliminar_recurso(self, codigo_recurso):
        """Solicita al servicio eliminar un recurso alimenticio por código."""
        return self.servicio_recurso.eliminar_recurso(codigo_recurso)

#---------------------------------------------------------------------------------------------

    def listar_recursos_por_categoria(self, categoria):
        """Solicita al servicio listar recursos alimenticios por categoría."""
        return self.servicio_recurso.listar_recursos_por_categoria(categoria)

#---------------------------------------------------------------------------------------------

    # ENTREGAS ALIMENTARIAS:

    def registrar_entrega(self, codigo_entrega, identificacion_beneficiario,
                          codigo_recurso, cantidad_entregada, fecha,
                          responsable_entrega):
        """Solicita al servicio registrar una entrega alimentaria."""
        return self.servicio_entrega.registrar_entrega(
            codigo_entrega,
            identificacion_beneficiario,
            codigo_recurso,
            cantidad_entregada,
            fecha,
            responsable_entrega
        )

#---------------------------------------------------------------------------------------------

    def consultar_entregas(self):
        """Solicita al servicio todas las entregas alimentarias registradas."""
        return self.servicio_entrega.consultar_entregas()

#---------------------------------------------------------------------------------------------

    def listar_entregas_por_beneficiario(self, identificacion_beneficiario):
        """Solicita al servicio listar entregas por beneficiario."""
        return self.servicio_entrega.listar_entregas_por_beneficiario(
            identificacion_beneficiario
        )

#---------------------------------------------------------------------------------------------

    def listar_entregas_por_fecha(self, fecha):
        """Solicita al servicio listar entregas por fecha."""
        return self.servicio_entrega.listar_entregas_por_fecha(fecha)

#---------------------------------------------------------------------------------------------

    def historial_entregas(self):
        """Solicita al servicio el historial completo de entregas alimentarias."""
        return self.servicio_entrega.historial_entregas()

#---------------------------------------------------------------------------------------------

    # REPORTES:

    def reporte_beneficiarios_por_comunidad(self):
        """Solicita al servicio el reporte de beneficiarios por comunidad."""
        return self.servicio_reporte.reporte_beneficiarios_por_comunidad()

#---------------------------------------------------------------------------------------------

    def reporte_recursos_inventario_bajo(self, limite):
        """Solicita al servicio el reporte de recursos con inventario bajo."""
        return self.servicio_reporte.reporte_recursos_inventario_bajo(limite)

#---------------------------------------------------------------------------------------------

    def reporte_recursos_mas_entregados(self):
        """Solicita al servicio el reporte de recursos más entregados."""
        return self.servicio_reporte.reporte_recursos_mas_entregados()

#---------------------------------------------------------------------------------------------

    def reporte_costo_total_ayuda_distribuida(self):
        """Solicita al servicio el reporte del costo total de ayuda distribuida."""
        return self.servicio_reporte.reporte_costo_total_ayuda_distribuida()

#---------------------------------------------------------------------------------------------