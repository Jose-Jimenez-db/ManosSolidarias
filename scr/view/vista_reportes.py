import tkinter as tk
from tkinter import ttk

#---------------------------------------------------------------------------------------------

class VistaReportes:

#---------------------------------------------------------------------------------------------

    def __init__(self, root, controlador):

        # Guarda controlador
        self.controlador = controlador

        # Crea ventana
        self.window = tk.Toplevel(root)

        # Configuración ventana
        self.window.title("Reportes del Sistema")

        # Tamaño ventana
        self.window.geometry("1000x600")

        # Evita redimensionar
        self.window.resizable(False, False)

        # Construye interfaz
        self._build_ui()

#---------------------------------------------------------------------------------------------

    def _build_ui(self):

        # Frame principal
        frame = ttk.Frame(self.window, padding=15)

        frame.pack(fill="both", expand=True)

        # Título principal
        ttk.Label(
            frame,
            text="Reportes del Sistema",
            font=("Arial", 15, "bold")
        ).pack(pady=10)

    #-------------------------------------------------------------------------------------
        # BOTONES
    #-------------------------------------------------------------------------------------

        # Frame para botones de reportes
        frame_botones = ttk.LabelFrame(
            frame,
            text="Reportes Disponibles",
            padding=15
        )

        frame_botones.pack(fill="x", pady=10)

        # Botón beneficiarios por comunidad
        ttk.Button(
            frame_botones,
            text="Beneficiarios por comunidad",
            width=32,
            command=self.reporte_comunidad
        ).grid(row=0, column=0, padx=5, pady=5)

        # Botón inventario bajo
        ttk.Button(
            frame_botones,
            text="Recursos con inventario bajo (>10)",
            width=32,
            command=self.reporte_stock
        ).grid(row=0, column=1, padx=5, pady=5)

        # Botón recursos más entregados
        ttk.Button(
            frame_botones,
            text="Top de recursos más entregados",
            width=32,
            command=self.reporte_top
        ).grid(row=0, column=2, padx=5, pady=5)

        # Botón costo total ayudas
        ttk.Button(
            frame_botones,
            text="Costo total de ayuda distribuida",
            width=32,
            command=self.reporte_costo
        ).grid(row=0, column=3, padx=5, pady=5)

    #-------------------------------------------------------------------------------------
        # TABLA
    #-------------------------------------------------------------------------------------

        # Treeview resultados
        self.tree = ttk.Treeview(
            frame,
            show="headings",
            height=20
        )

        self.tree.pack(fill="x", pady=15)

#---------------------------------------------------------------------------------------------

    def limpiar_tabla(self):

        # Elimina filas
        for item in self.tree.get_children():
            self.tree.delete(item)

#---------------------------------------------------------------------------------------------

    def configurar_tabla(self, columnas, encabezados):

        # Configura columnas de la tabla según el reporte seleccionado
        self.tree["columns"] = columnas

        # Configura encabezados y tamaños de columnas
        for columna, encabezado in zip(columnas, encabezados):

            self.tree.heading(
                columna,
                text=encabezado,
                anchor="center"
            )

            self.tree.column(
                columna,
                width=280,
                anchor="center"
            )

#---------------------------------------------------------------------------------------------

    def reporte_comunidad(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Configura tabla
        self.configurar_tabla(
            ("comunidad", "cantidad"),
            ("Comunidad", "Cantidad de beneficiarios")
        )

        # Consulta reporte
        lista = self.controlador.reporte_beneficiarios_por_comunidad()

        # Inserta resultados
        for comunidad, cantidad in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(comunidad, cantidad)
            )

#---------------------------------------------------------------------------------------------

    def reporte_stock(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Configura tabla
        self.configurar_tabla(
            ("codigo", "nombre", "cantidad"),
            ("Código recurso", "Nombre recurso", "Cantidad disponible")
        )

        # Consulta reporte
        lista = self.controlador.reporte_recursos_inventario_bajo(10)

        # Inserta resultados
        for codigo, nombre, cantidad in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(codigo, nombre, cantidad)
            )

#---------------------------------------------------------------------------------------------

    def reporte_top(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Configura tabla
        self.configurar_tabla(
            ("recurso", "cantidad"),
            ("Recurso", "Cantidad entregada")
        )

        # Consulta reporte
        lista = self.controlador.reporte_recursos_mas_entregados()

        # Inserta resultados
        for recurso, cantidad in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(recurso, cantidad)
            )

#---------------------------------------------------------------------------------------------

    def reporte_costo(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Configura tabla
        self.configurar_tabla(
            ("concepto", "costo"),
            ("Concepto", "Costo total")
        )

        # Obtiene costo total
        total = self.controlador.reporte_costo_total_ayuda_distribuida()

        # Inserta resultado
        self.tree.insert(
            "",
            tk.END,
            values=("Ayuda distribuida", total)
        )

#---------------------------------------------------------------------------------------------