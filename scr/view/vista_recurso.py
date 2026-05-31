import tkinter as tk
from tkinter import ttk, messagebox

#---------------------------------------------------------------------------------------------

class VistaRecurso:

#---------------------------------------------------------------------------------------------

    def __init__(self, root, controlador):

        # Guarda controlador
        self.controlador = controlador

        # Crea ventana
        self.window = tk.Toplevel(root)

        # Configuración ventana
        self.window.title("Gestión de Recursos Alimenticios")

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
            text="Gestión de Recursos Alimenticios",
            font=("Arial", 15, "bold")
        ).pack(pady=10)

    #-------------------------------------------------------------------------------------
        # CAMPOS
    #-------------------------------------------------------------------------------------

        # Frame para campos del formulario
        frame_campos = ttk.LabelFrame(
            frame,
            text="Datos del Recurso Alimenticio",
            padding=15
        )

        frame_campos.pack(fill="x", pady=10)

        # Etiqueta código recurso
        ttk.Label(
            frame_campos,
            text="Código recurso:"
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Caja texto código recurso
        self.entry_codigo = ttk.Entry(frame_campos, width=30)

        self.entry_codigo.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta nombre
        ttk.Label(
            frame_campos,
            text="Nombre:"
        ).grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Caja texto nombre
        self.entry_nombre = ttk.Entry(frame_campos, width=30)

        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta categoría
        ttk.Label(
            frame_campos,
            text="Categoría:"
        ).grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Caja texto categoría
        self.entry_categoria = ttk.Entry(frame_campos, width=30)

        self.entry_categoria.grid(row=2, column=1, padx=10, pady=5)

        # Etiqueta cantidad disponible
        ttk.Label(
            frame_campos,
            text="Cantidad disponible:"
        ).grid(row=0, column=2, padx=10, pady=5, sticky="w")

        # Caja texto cantidad disponible
        self.entry_cantidad = ttk.Entry(frame_campos, width=30)

        self.entry_cantidad.grid(row=0, column=3, padx=10, pady=5)

        # Etiqueta costo unitario
        ttk.Label(
            frame_campos,
            text="Costo unitario:"
        ).grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Caja texto costo unitario
        self.entry_costo = ttk.Entry(frame_campos, width=30)

        self.entry_costo.grid(row=1, column=3, padx=10, pady=5)

    #-------------------------------------------------------------------------------------
        # BOTONES
    #-------------------------------------------------------------------------------------

        # Frame para botones
        frame_botones = ttk.Frame(frame)

        frame_botones.pack(pady=10)

        # Botón registrar recurso
        ttk.Button(
            frame_botones,
            text="Registrar",
            command=self.registrar
        ).grid(row=0, column=0, padx=5)

        # Botón buscar por código
        ttk.Button(
            frame_botones,
            text="Buscar por código",
            command=self.buscar_codigo
        ).grid(row=0, column=1, padx=5)

        # Botón buscar por categoría
        ttk.Button(
            frame_botones,
            text="Buscar por categoría",
            command=self.buscar_categoria
        ).grid(row=0, column=2, padx=5)

        # Botón consultar todos
        ttk.Button(
            frame_botones,
            text="Consultar todos",
            command=self.consultar_todos
        ).grid(row=0, column=3, padx=5)

        # Botón eliminar recurso
        ttk.Button(
            frame_botones,
            text="Eliminar",
            command=self.eliminar
        ).grid(row=0, column=4, padx=5)

        # Botón limpiar campos
        ttk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar_campos
        ).grid(row=0, column=5, padx=5)

    #-------------------------------------------------------------------------------------
        # TABLA
    #-------------------------------------------------------------------------------------

        # Columnas tabla
        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "cantidad",
            "costo"
        )

        # Treeview resultados
        self.tree = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            height=14
        )

        self.tree.pack(fill="x", pady=15)

        # Encabezados tabla
        self.tree.heading("codigo", text="Código", anchor="center")
        self.tree.heading("nombre", text="Nombre", anchor="center")
        self.tree.heading("categoria", text="Categoría", anchor="center")
        self.tree.heading("cantidad", text="Cantidad", anchor="center")
        self.tree.heading("costo", text="Costo", anchor="center")

        # Tamaño columnas
        self.tree.column("codigo", width=130, anchor="center")
        self.tree.column("nombre", width=240, anchor="center")
        self.tree.column("categoria", width=180, anchor="center")
        self.tree.column("cantidad", width=120, anchor="center")
        self.tree.column("costo", width=120, anchor="center")

#---------------------------------------------------------------------------------------------

    def limpiar_tabla(self):

        # Elimina filas tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

#---------------------------------------------------------------------------------------------

    def limpiar_campos(self):

        # Limpia las cajas de texto
        self.entry_codigo.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_costo.delete(0, tk.END)

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
                "Recurso registrado correctamente!"
            )

            # Limpia campos
            self.limpiar_campos()

        except ValueError as e:

            # Muestra error validación
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

        else:

            # Muestra mensaje si no existe
            messagebox.showinfo(
                "Resultado",
                "No se encontró un recurso con ese código..."
            )

#---------------------------------------------------------------------------------------------

    def buscar_categoria(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Busca categoría
        lista = self.controlador.listar_recursos_por_categoria(
            self.entry_categoria.get()
        )

        # Verifica si hay resultados
        if len(lista) == 0:

            # Muestra mensaje si no hay resultados
            messagebox.showinfo(
                "Resultado",
                "No se encontraron recursos en esa categoría..."
            )

            return

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

#---------------------------------------------------------------------------------------------

    def eliminar(self):

        try:

            # Pregunta confirmación antes de eliminar
            confirmacion = messagebox.askyesno(
                "Confirmar eliminación",
                "¿Está seguro de que desea eliminar este recurso?"
            )

            # Si el usuario no confirma, se cancela el proceso
            if not confirmacion:
                return

            # Elimina recurso por código
            self.controlador.eliminar_recurso(
                self.entry_codigo.get()
            )

            # Mensaje éxito
            messagebox.showinfo(
                "Éxito",
                "Recurso eliminado correctamente!"
            )

            # Limpia campos
            self.limpiar_campos()

            # Actualiza tabla
            self.consultar_todos()

        except ValueError as e:

            # Muestra error validación
            messagebox.showerror(
                "Error",
                str(e)
            )

#---------------------------------------------------------------------------------------------