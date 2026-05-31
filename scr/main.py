import tkinter as tk

# REPOSITORIOS

from scr.repository.repositorio import Repositorio

# SERVICIOS

from scr.service.servicio_usuario import ServicioUsuario
from scr.service.servicio_beneficiario import ServicioBeneficiario
from scr.service.servicio_recurso import ServicioRecurso
from scr.service.servicio_entrega import ServicioEntrega
from scr.service.servicio_reportes import ServicioReporte

# CONTROLADOR

from scr.controller.controlador import Controlador

# VISTAS

from scr.view.vista_inicio_sesion import VistaInicioSesion

#---------------------------------------------------------------------------------------------

def main():

    # Ventana raíz
    root = tk.Tk()

    # Oculta ventana vacía
    root.withdraw()

    # REPOSITORIOS

    repo_usuarios = Repositorio(
        "data/usuarios.json"
    )

    repo_beneficiarios = Repositorio(
        "data/beneficiarios.json"
    )

    repo_recursos = Repositorio(
        "data/recursos.json"
    )

    repo_entregas = Repositorio(
        "data/entregas.json"
    )

    # SERVICIOS

    servicio_usuario = ServicioUsuario(
        repo_usuarios
    )

    servicio_beneficiario = ServicioBeneficiario(
        repo_beneficiarios
    )

    servicio_recurso = ServicioRecurso(
        repo_recursos
    )

    servicio_entrega = ServicioEntrega(
        repo_entregas,
        repo_beneficiarios,
        repo_recursos
    )

    servicio_reporte = ServicioReporte(
        repo_beneficiarios,
        repo_recursos,
        repo_entregas
    )

    # CONTROLADOR

    controlador = Controlador(
        servicio_usuario,
        servicio_beneficiario,
        servicio_recurso,
        servicio_entrega,
        servicio_reporte
    )

    # VISTA LOGIN

    VistaInicioSesion(
        root,
        controlador
    )

    # Ejecuta aplicación
    root.mainloop()

#---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

#---------------------------------------------------------------------------------------------