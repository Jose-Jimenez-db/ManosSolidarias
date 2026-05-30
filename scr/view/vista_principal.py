import tkinter as tk
from tkinter import ttk

from view.vista_beneficiario import VistaBeneficiario
from view.vista_recurso import VistaRecurso
from view.vista_entrega import VistaEntrega
from view.vista_reportes import VistaReportes

#---------------------------------------------------------------------------------------------

class VistaPrincipal:

    def __init__(self, root, controlador):

        # Guarda referencia del controlador
        self.controlador = controlador

        # Crea ventana principal
        self.window = tk.Toplevel(root)

        # Título ventana
        self.window.title("Sistema Manos Solidarias")

        # Tamaño ventana
        self.window.geometry("500x400")

        # Evita redimensionar
        self.window.resizable(False, False)

        # Construye interfaz
        self._build_ui()

#---------------------------------------------------------------------------------------------

    def _build_ui(self):

        # Frame principal
        frame = ttk.Frame(self.window, padding=30)

        frame.pack(fill="both", expand=True)

        # Título principal
        ttk.Label(
            frame,
            text="Sistema Manos Solidarias",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        # Botón abrir beneficiarios
        ttk.Button(
            frame,
            text="Gestión Beneficiarios",
            width=30,
            command=self.abrir_beneficiarios
        ).pack(pady=10)

        # Botón abrir recursos
        ttk.Button(
            frame,
            text="Gestión Recursos",
            width=30,
            command=self.abrir_recursos
        ).pack(pady=10)

        # Botón abrir entregas
        ttk.Button(
            frame,
            text="Gestión Entregas",
            width=30,
            command=self.abrir_entregas
        ).pack(pady=10)

        # Botón abrir reportes
        ttk.Button(
            frame,
            text="Reportes",
            width=30,
            command=self.abrir_reportes
        ).pack(pady=10)

        # Botón salir
        ttk.Button(
            frame,
            text="Salir",
            width=30,
            command=self.window.destroy
        ).pack(pady=10)

#---------------------------------------------------------------------------------------------

    def abrir_beneficiarios(self):

        # Abre ventana beneficiarios
        VistaBeneficiario(
            self.window,
            self.controlador
        )

#---------------------------------------------------------------------------------------------

    def abrir_recursos(self):

        # Abre ventana recursos
        VistaRecurso(
            self.window,
            self.controlador
        )

#---------------------------------------------------------------------------------------------

    def abrir_entregas(self):

        # Abre ventana entregas
        VistaEntrega(
            self.window,
            self.controlador
        )

#---------------------------------------------------------------------------------------------

    def abrir_reportes(self):

        # Abre ventana reportes
        VistaReportes(
            self.window,
            self.controlador
        )