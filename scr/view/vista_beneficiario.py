import tkinter as tk
from tkinter import ttk, messagebox

#---------------------------------------------------------------------------------------------

class VistaBeneficiario:

#---------------------------------------------------------------------------------------------

    def __init__(self, root, controlador):

        # Guarda referencia del controlador
        self.controlador = controlador

        # Crea ventana beneficiarios
        self.window = tk.Toplevel(root)

        # Título ventana
        self.window.title("Gestión de Beneficiarios")

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
            text="Gestión de Beneficiarios",
            font=("Arial", 15, "bold")
        ).pack(pady=10)

    #-------------------------------------------------------------------------------------
        # CAMPOS
    #-------------------------------------------------------------------------------------

        # Frame para campos del formulario
        frame_campos = ttk.LabelFrame(
            frame,
            text="Datos del Beneficiario",
            padding=15
        )

        frame_campos.pack(fill="x", pady=10)

        # Etiqueta identificación
        ttk.Label(
            frame_campos,
            text="Identificación:"
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Caja texto identificación
        self.txt_identificacion = ttk.Entry(frame_campos, width=30)

        self.txt_identificacion.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta nombre
        ttk.Label(
            frame_campos,
            text="Nombre completo:"
        ).grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Caja texto nombre
        self.txt_nombre = ttk.Entry(frame_campos, width=30)

        self.txt_nombre.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta comunidad
        ttk.Label(
            frame_campos,
            text="Comunidad:"
        ).grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Caja texto comunidad
        self.txt_comunidad = ttk.Entry(frame_campos, width=30)

        self.txt_comunidad.grid(row=2, column=1, padx=10, pady=5)

        # Etiqueta integrantes hogar
        ttk.Label(
            frame_campos,
            text="Integrantes hogar:"
        ).grid(row=0, column=2, padx=10, pady=5, sticky="w")

        # Caja texto integrantes
        self.txt_integrantes = ttk.Entry(frame_campos, width=30)

        self.txt_integrantes.grid(row=0, column=3, padx=10, pady=5)

        # Etiqueta prioridad social
        ttk.Label(
            frame_campos,
            text="Prioridad social:"
        ).grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Caja texto prioridad
        self.txt_prioridad = ttk.Entry(frame_campos, width=30)

        self.txt_prioridad.grid(row=1, column=3, padx=10, pady=5)

    #-------------------------------------------------------------------------------------
        # BOTONES
    #-------------------------------------------------------------------------------------

        # Frame para botones
        frame_botones = ttk.Frame(frame)

        frame_botones.pack(pady=10)

        # Botón registrar beneficiario
        ttk.Button(
            frame_botones,
            text="Registrar",
            command=self.registrar
        ).grid(row=0, column=0, padx=5)

        # Botón buscar por identificación
        ttk.Button(
            frame_botones,
            text="Buscar por ID",
            command=self.buscar_id
        ).grid(row=0, column=1, padx=5)

        # Botón buscar por comunidad
        ttk.Button(
            frame_botones,
            text="Buscar por comunidad",
            command=self.buscar_comunidad
        ).grid(row=0, column=2, padx=5)

        # Botón consultar todos
        ttk.Button(
            frame_botones,
            text="Consultar todos",
            command=self.consultar_todos
        ).grid(row=0, column=3, padx=5)

        # Botón eliminar beneficiario
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
            "id",
            "nombre",
            "comunidad",
            "integrantes",
            "prioridad"
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
        self.tree.heading("id", text="Identificación", anchor="center")
        self.tree.heading("nombre", text="Nombre", anchor="center")
        self.tree.heading("comunidad", text="Comunidad", anchor="center")
        self.tree.heading("integrantes", text="Integrantes", anchor="center")
        self.tree.heading("prioridad", text="Prioridad", anchor="center")

        # Tamaño columnas
        self.tree.column("id", width=130, anchor="center")
        self.tree.column("nombre", width=240, anchor="center")
        self.tree.column("comunidad", width=180, anchor="center")
        self.tree.column("integrantes", width=120, anchor="center")
        self.tree.column("prioridad", width=120, anchor="center")

#---------------------------------------------------------------------------------------------

    def limpiar_tabla(self):

        # Elimina filas anteriores
        for item in self.tree.get_children():
            self.tree.delete(item)

#---------------------------------------------------------------------------------------------

    def limpiar_campos(self):

        # Limpia las cajas de texto
        self.txt_identificacion.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_comunidad.delete(0, tk.END)
        self.txt_integrantes.delete(0, tk.END)
        self.txt_prioridad.delete(0, tk.END)

#---------------------------------------------------------------------------------------------

    def registrar(self):

        try:

            # Registra beneficiario
            self.controlador.registrar_beneficiario(
                self.txt_identificacion.get(),
                self.txt_nombre.get(),
                self.txt_comunidad.get(),
                self.txt_integrantes.get(),
                self.txt_prioridad.get()
            )

            # Mensaje éxito
            messagebox.showinfo(
                "Éxito",
                "Beneficiario registrado correctamente!"
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

        # Obtiene beneficiarios
        lista = self.controlador.consultar_beneficiarios()

        # Inserta resultados
        for beneficiario in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    beneficiario.identificacion,
                    beneficiario.nombre_completo,
                    beneficiario.comunidad,
                    beneficiario.integrantes_hogar,
                    beneficiario.prioridad_social
                )
            )

#---------------------------------------------------------------------------------------------

    def buscar_id(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Busca beneficiario por identificación
        beneficiario = self.controlador.buscar_beneficiario(
            self.txt_identificacion.get()
        )

        # Verifica si existe
        if beneficiario is not None:

            # Inserta resultado tabla
            self.tree.insert(
                "",
                tk.END,
                values=(
                    beneficiario.identificacion,
                    beneficiario.nombre_completo,
                    beneficiario.comunidad,
                    beneficiario.integrantes_hogar,
                    beneficiario.prioridad_social
                )
            )

        else:

            # Muestra mensaje si no existe
            messagebox.showinfo(
                "Resultado",
                "No se encontró un beneficiario con esa identificación..."
            )

#---------------------------------------------------------------------------------------------

    def buscar_comunidad(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Busca beneficiarios comunidad
        lista = self.controlador.listar_beneficiarios_por_comunidad(
            self.txt_comunidad.get()
        )

        # Verifica si hay resultados
        if len(lista) == 0:

            # Muestra mensaje si no hay resultados
            messagebox.showinfo(
                "Resultado",
                "No se encontraron beneficiarios en esa comunidad..."
            )

            return

        # Inserta resultados
        for beneficiario in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    beneficiario.identificacion,
                    beneficiario.nombre_completo,
                    beneficiario.comunidad,
                    beneficiario.integrantes_hogar,
                    beneficiario.prioridad_social
                )
            )

#---------------------------------------------------------------------------------------------

    def eliminar(self):

        try:

            # Pregunta confirmación antes de eliminar
            confirmacion = messagebox.askyesno(
                "Confirmar eliminación",
                "¿Está seguro de que desea eliminar este beneficiario?"
            )

            # Si el usuario no confirma, se cancela el proceso
            if not confirmacion:
                return

            # Elimina beneficiario por identificación
            self.controlador.eliminar_beneficiario(
                self.txt_identificacion.get()
            )

            # Mensaje éxito
            messagebox.showinfo(
                "Éxito",
                "Beneficiario eliminado correctamente!"
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