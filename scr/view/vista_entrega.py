import tkinter as tk
from tkinter import ttk, messagebox

#---------------------------------------------------------------------------------------------

class VistaEntrega:

    def __init__(self, root, controlador):

        # Guarda controlador
        self.controlador = controlador

        # Crea ventana
        self.window = tk.Toplevel(root)

        # Configuración ventana
        self.window.title("Gestión Entregas")

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

        # Título centrado
        ttk.Label(
            frame,
            text="Gestión Entregas Alimentarias",
            font=("Arial", 16, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            pady=20
        )

        # Labels y entries

        ttk.Label(
            frame,
            text="Código Entrega:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=8
        )

        self.entry_codigo = ttk.Entry(
            frame,
            width=30
        )

        self.entry_codigo.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        ttk.Label(
            frame,
            text="ID Beneficiario:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=8
        )

        self.entry_beneficiario = ttk.Entry(
            frame,
            width=30
        )

        self.entry_beneficiario.grid(
            row=2,
            column=1,
            padx=10,
            pady=8
        )

        ttk.Label(
            frame,
            text="Código Recurso:"
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=8
        )

        self.entry_recurso = ttk.Entry(
            frame,
            width=30
        )

        self.entry_recurso.grid(
            row=3,
            column=1,
            padx=10,
            pady=8
        )

        ttk.Label(
            frame,
            text="Cantidad:"
        ).grid(
            row=4,
            column=0,
            padx=10,
            pady=8
        )

        self.entry_cantidad = ttk.Entry(
            frame,
            width=30
        )

        self.entry_cantidad.grid(
            row=4,
            column=1,
            padx=10,
            pady=8
        )

        # BOTONES

        ttk.Button(
            frame,
            text="Registrar",
            width=20,
            command=self.registrar
        ).grid(
            row=5,
            column=0,
            pady=15
        )

        ttk.Button(
            frame,
            text="Buscar Beneficiario",
            width=20,
            command=self.buscar_beneficiario
        ).grid(
            row=5,
            column=1,
            pady=15
        )

        ttk.Button(
            frame,
            text="Buscar Fecha",
            width=20,
            command=self.buscar_fecha
        ).grid(
            row=5,
            column=2,
            pady=15
        )

        ttk.Button(
            frame,
            text="Consultar Todos",
            width=20,
            command=self.consultar_todos
        ).grid(
            row=5,
            column=3,
            pady=15
        )

        # TABLA

        columnas = (
            "codigo",
            "beneficiario",
            "recurso",
            "cantidad"
        )

        self.tree = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            height=12
        )

        self.tree.grid(
            row=6,
            column=0,
            columnspan=4,
            padx=10,
            pady=20
        )

        # Encabezados tabla

        self.tree.heading("codigo", text="Código")
        self.tree.heading("beneficiario", text="Beneficiario")
        self.tree.heading("recurso", text="Recurso")
        self.tree.heading("cantidad", text="Cantidad")

        # Tamaños columnas

        self.tree.column("codigo", width=150)
        self.tree.column("beneficiario", width=250)
        self.tree.column("recurso", width=250)
        self.tree.column("cantidad", width=120)

#---------------------------------------------------------------------------------------------

    def limpiar_tabla(self):

        # Elimina filas tabla
        for item in self.tree.get_children():

            self.tree.delete(item)

#---------------------------------------------------------------------------------------------

    def registrar(self):

        try:

            # Registra entrega
            self.controlador.registrar_entrega(
                self.entry_codigo.get(),
                self.entry_beneficiario.get(),
                self.entry_recurso.get(),
                self.entry_cantidad.get(),
                "2026-05-30",
                "Administrador"
            )

            # Mensaje éxito
            messagebox.showinfo(
                "Éxito",
                "Entrega registrada correctamente"
            )

            # Actualiza tabla
            self.consultar_todos()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

#---------------------------------------------------------------------------------------------

    def consultar_todos(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Consulta entregas
        lista = self.controlador.consultar_entregas()

        # Inserta resultados
        for entrega in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    entrega.codigo_entrega,
                    entrega.identificacion_beneficiario,
                    entrega.codigo_recurso,
                    entrega.cantidad_entregada
                )
            )

#---------------------------------------------------------------------------------------------

    def buscar_beneficiario(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Busca entregas beneficiario
        lista = self.controlador.listar_entregas_por_beneficiario(
            self.entry_beneficiario.get()
        )

        # Inserta resultados
        for entrega in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    entrega.codigo_entrega,
                    entrega.identificacion_beneficiario,
                    entrega.codigo_recurso,
                    entrega.cantidad_entregada
                )
            )

#---------------------------------------------------------------------------------------------

    def buscar_fecha(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Busca entregas fecha
        lista = self.controlador.listar_entregas_por_fecha(
            "2026-05-30"
        )

        # Inserta resultados
        for entrega in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    entrega.codigo_entrega,
                    entrega.identificacion_beneficiario,
                    entrega.codigo_recurso,
                    entrega.cantidad_entregada
                )
            )