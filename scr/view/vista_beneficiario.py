# view/vista_beneficiario.py

import tkinter as tk
from tkinter import ttk, messagebox

#---------------------------------------------------------------------------------------------

class VistaBeneficiario:

    def __init__(self, root, controlador):

        # Guarda referencia del controlador
        self.controlador = controlador

        # Crea ventana beneficiarios
        self.window = tk.Toplevel(root)

        # Título ventana
        self.window.title("Gestión Beneficiarios")

        # Tamaño ventana
        self.window.geometry("950x550")

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
            text="Gestión Beneficiarios",
            font=("Arial", 15, "bold")
        ).grid(row=0, column=0, columnspan=4, pady=15)

        #-------------------------------------------------------------------------------------
        # CAMPOS
        #-------------------------------------------------------------------------------------

        # Etiqueta identificación
        ttk.Label(
            frame,
            text="Identificación"
        ).grid(row=1, column=0)

        # Caja texto identificación
        self.txt_identificacion = ttk.Entry(frame, width=30)

        self.txt_identificacion.grid(row=1, column=1)

        # Etiqueta nombre
        ttk.Label(
            frame,
            text="Nombre completo"
        ).grid(row=2, column=0)

        # Caja texto nombre
        self.txt_nombre = ttk.Entry(frame, width=30)

        self.txt_nombre.grid(row=2, column=1)

        # Etiqueta comunidad
        ttk.Label(
            frame,
            text="Comunidad"
        ).grid(row=3, column=0)

        # Caja texto comunidad
        self.txt_comunidad = ttk.Entry(frame, width=30)

        self.txt_comunidad.grid(row=3, column=1)

        # Etiqueta integrantes hogar
        ttk.Label(
            frame,
            text="Integrantes hogar"
        ).grid(row=1, column=2)

        # Caja texto integrantes
        self.txt_integrantes = ttk.Entry(frame, width=30)

        self.txt_integrantes.grid(row=1, column=3)

        # Etiqueta prioridad social
        ttk.Label(
            frame,
            text="Prioridad social"
        ).grid(row=2, column=2)

        # Caja texto prioridad
        self.txt_prioridad = ttk.Entry(frame, width=30)

        self.txt_prioridad.grid(row=2, column=3)

        #-------------------------------------------------------------------------------------
        # BOTONES
        #-------------------------------------------------------------------------------------

        # Botón registrar beneficiario
        ttk.Button(
            frame,
            text="Registrar",
            command=self.registrar
        ).grid(row=4, column=0, pady=10)

        # Botón buscar por identificación
        ttk.Button(
            frame,
            text="Buscar por ID",
            command=self.buscar_id
        ).grid(row=4, column=1)

        # Botón buscar por comunidad
        ttk.Button(
            frame,
            text="Buscar comunidad",
            command=self.buscar_comunidad
        ).grid(row=4, column=2)

        # Botón consultar todos
        ttk.Button(
            frame,
            text="Consultar todos",
            command=self.consultar_todos
        ).grid(row=4, column=3)

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
            height=12
        )

        self.tree.grid(
            row=5,
            column=0,
            columnspan=4,
            pady=15
        )

        # Encabezados tabla
        self.tree.heading("id", text="Identificación")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("comunidad", text="Comunidad")
        self.tree.heading("integrantes", text="Integrantes")
        self.tree.heading("prioridad", text="Prioridad")

#---------------------------------------------------------------------------------------------

    def limpiar_tabla(self):

        # Elimina filas anteriores
        for item in self.tree.get_children():
            self.tree.delete(item)

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
                "Beneficiario registrado correctamente"
            )

            # Actualiza tabla
            self.consultar_todos()

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

#---------------------------------------------------------------------------------------------

    def buscar_comunidad(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Busca beneficiarios comunidad
        lista = self.controlador.listar_beneficiarios_por_comunidad(
            self.txt_comunidad.get()
        )

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
