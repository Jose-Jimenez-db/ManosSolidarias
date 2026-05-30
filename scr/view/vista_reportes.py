import tkinter as tk
from tkinter import ttk

#---------------------------------------------------------------------------------------------

class VistaReportes:

    def __init__(self, root, controlador):

        # Guarda controlador
        self.controlador = controlador

        # Crea ventana
        self.window = tk.Toplevel(root)

        # Configuración ventana
        self.window.title("Reportes")

        self.window.geometry("1000x600")

        self.window.resizable(False, False)

        # Construye interfaz
        self._build_ui()

#---------------------------------------------------------------------------------------------

    def _build_ui(self):

        # Frame principal
        frame = ttk.Frame(
            self.window,
            padding=20
        )

        frame.pack(fill="both", expand=True)

        # Título
        ttk.Label(
            frame,
            text="Reportes del Sistema",
            font=("Arial", 16, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            pady=20
        )

        # BOTONES

        ttk.Button(
            frame,
            text="Beneficiarios por Comunidad",
            width=28,
            command=self.reporte_comunidad
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        ttk.Button(
            frame,
            text="Inventario Bajo",
            width=28,
            command=self.reporte_stock
        ).grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Button(
            frame,
            text="Recursos Más Entregados",
            width=28,
            command=self.reporte_top
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=10
        )

        ttk.Button(
            frame,
            text="Costo Total Ayudas",
            width=28,
            command=self.reporte_costo
        ).grid(
            row=1,
            column=3,
            padx=10,
            pady=10
        )

        # TABLA

        columnas = (
            "dato1",
            "dato2",
            "dato3"
        )

        self.tree = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            height=15
        )

        self.tree.grid(
            row=2,
            column=0,
            columnspan=4,
            padx=10,
            pady=20
        )

        # Encabezados

        self.tree.heading("dato1", text="Dato 1")
        self.tree.heading("dato2", text="Dato 2")
        self.tree.heading("dato3", text="Dato 3")

        # Tamaños columnas

        self.tree.column("dato1", width=280)
        self.tree.column("dato2", width=280)
        self.tree.column("dato3", width=280)

#---------------------------------------------------------------------------------------------

    def limpiar_tabla(self):

        # Elimina filas
        for item in self.tree.get_children():

            self.tree.delete(item)

#---------------------------------------------------------------------------------------------

    def reporte_comunidad(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Consulta reporte
        lista = self.controlador.reporte_beneficiarios_por_comunidad()

        # Inserta resultados
        for dato in lista:

            self.tree.insert(
                "",
                tk.END,
                values=dato
            )

#---------------------------------------------------------------------------------------------

    def reporte_stock(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Consulta reporte
        lista = self.controlador.reporte_recursos_inventario_bajo(10)

        # Inserta resultados
        for dato in lista:

            self.tree.insert(
                "",
                tk.END,
                values=dato
            )

#---------------------------------------------------------------------------------------------

    def reporte_top(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Consulta reporte
        lista = self.controlador.reporte_recursos_mas_entregados()

        # Inserta resultados
        for dato in lista:

            self.tree.insert(
                "",
                tk.END,
                values=dato
            )

#---------------------------------------------------------------------------------------------

    def reporte_costo(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Obtiene costo total
        total = self.controlador.reporte_costo_total_ayuda_distribuida()

        # Inserta resultado
        self.tree.insert(
            "",
            tk.END,
            values=("Costo Total", total, "")
        )