import tkinter as tk
from tkinter import ttk, messagebox

#---------------------------------------------------------------------------------------------

class VistaRecurso:

    def __init__(self, root, controlador):

        # Guarda controlador
        self.controlador = controlador

        # Crea ventana
        self.window = tk.Toplevel(root)

        # Configuración ventana
        self.window.title("Gestión Recursos Alimenticios")

        self.window.geometry("1050x620")

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

        #-------------------------------------------------------------------------------------
        # TÍTULO
        #-------------------------------------------------------------------------------------

        ttk.Label(
            frame,
            text="Gestión Recursos Alimenticios",
            font=("Arial", 16, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            pady=20
        )

        #-------------------------------------------------------------------------------------
        # LABELS Y ENTRIES
        #-------------------------------------------------------------------------------------

        # Código recurso
        ttk.Label(
            frame,
            text="Código recurso:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.entry_codigo = ttk.Entry(
            frame,
            width=32
        )

        self.entry_codigo.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        # Nombre recurso
        ttk.Label(
            frame,
            text="Nombre:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.entry_nombre = ttk.Entry(
            frame,
            width=32
        )

        self.entry_nombre.grid(
            row=2,
            column=1,
            padx=10,
            pady=8
        )

        # Categoría
        ttk.Label(
            frame,
            text="Categoría:"
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.entry_categoria = ttk.Entry(
            frame,
            width=32
        )

        self.entry_categoria.grid(
            row=3,
            column=1,
            padx=10,
            pady=8
        )

        # Cantidad
        ttk.Label(
            frame,
            text="Cantidad disponible:"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.entry_cantidad = ttk.Entry(
            frame,
            width=32
        )

        self.entry_cantidad.grid(
            row=1,
            column=3,
            padx=10,
            pady=8
        )

        # Costo
        ttk.Label(
            frame,
            text="Costo unitario:"
        ).grid(
            row=2,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.entry_costo = ttk.Entry(
            frame,
            width=32
        )

        self.entry_costo.grid(
            row=2,
            column=3,
            padx=10,
            pady=8
        )

        #-------------------------------------------------------------------------------------
        # BOTONES
        #-------------------------------------------------------------------------------------

        ttk.Button(
            frame,
            text="Registrar",
            width=20,
            command=self.registrar
        ).grid(
            row=4,
            column=0,
            pady=20
        )

        ttk.Button(
            frame,
            text="Buscar Código",
            width=20,
            command=self.buscar_codigo
        ).grid(
            row=4,
            column=1,
            pady=20
        )

        ttk.Button(
            frame,
            text="Buscar Categoría",
            width=20,
            command=self.buscar_categoria
        ).grid(
            row=4,
            column=2,
            pady=20
        )

        ttk.Button(
            frame,
            text="Consultar Todos",
            width=20,
            command=self.consultar_todos
        ).grid(
            row=4,
            column=3,
            pady=20
        )

        #-------------------------------------------------------------------------------------
        # TABLA
        #-------------------------------------------------------------------------------------

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "cantidad",
            "costo"
        )

        self.tree = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            height=14
        )

        self.tree.grid(
            row=5,
            column=0,
            columnspan=4,
            padx=10,
            pady=20
        )

        # Encabezados
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("categoria", text="Categoría")
        self.tree.heading("cantidad", text="Cantidad")
        self.tree.heading("costo", text="Costo")

        # Tamaños columnas
        self.tree.column("codigo", width=140)
        self.tree.column("nombre", width=250)
        self.tree.column("categoria", width=220)
        self.tree.column("cantidad", width=150)
        self.tree.column("costo", width=150)

#---------------------------------------------------------------------------------------------

    def limpiar_tabla(self):

        # Elimina filas tabla
        for item in self.tree.get_children():

            self.tree.delete(item)

#---------------------------------------------------------------------------------------------

    def registrar(self):

        try:

            # Registra recurso
            self.controlador.registrar_recurso(
                self.entry_codigo.get(),
                self.entry_nombre.get(),
                self.entry_categoria.get(),
                self.entry_cantidad.get(),
                self.entry_costo.get()
            )

            # Mensaje éxito
            messagebox.showinfo(
                "Éxito",
                "Recurso registrado correctamente"
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

        # Consulta recursos
        lista = self.controlador.consultar_recursos()

        # Inserta recursos tabla
        for recurso in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    recurso.codigo_recurso,
                    recurso.nombre,
                    recurso.categoria,
                    recurso.cantidad_disponible,
                    recurso.costo_unitario
                )
            )

#---------------------------------------------------------------------------------------------

    def buscar_codigo(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Busca recurso
        recurso = self.controlador.buscar_recurso(
            self.entry_codigo.get()
        )

        # Si existe
        if recurso is not None:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    recurso.codigo_recurso,
                    recurso.nombre,
                    recurso.categoria,
                    recurso.cantidad_disponible,
                    recurso.costo_unitario
                )
            )

#---------------------------------------------------------------------------------------------

    def buscar_categoria(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Busca categoría
        lista = self.controlador.listar_recursos_por_categoria(
            self.entry_categoria.get()
        )

        # Inserta resultados
        for recurso in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    recurso.codigo_recurso,
                    recurso.nombre,
                    recurso.categoria,
                    recurso.cantidad_disponible,
                    recurso.costo_unitario
                )
            )