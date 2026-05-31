import tkinter as tk
from tkinter import ttk, messagebox

#---------------------------------------------------------------------------------------------

class VistaEntrega:

#---------------------------------------------------------------------------------------------

    def __init__(self, root, controlador):

        # Guarda controlador
        self.controlador = controlador

        # Crea ventana
        self.window = tk.Toplevel(root)

        # Configuración ventana
        self.window.title("Gestión de Entregas Alimentarias")

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
            text="Gestión de Entregas Alimentarias",
            font=("Arial", 15, "bold")
        ).pack(pady=10)

    #-------------------------------------------------------------------------------------
        # CAMPOS
    #-------------------------------------------------------------------------------------

        # Frame para campos del formulario
        frame_campos = ttk.LabelFrame(
            frame,
            text="Datos de la Entrega Alimentaria",
            padding=15
        )

        frame_campos.pack(fill="x", pady=10)

        # Etiqueta código entrega
        ttk.Label(
            frame_campos,
            text="Código entrega:"
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Caja texto código entrega
        self.entry_codigo = ttk.Entry(frame_campos, width=30)

        self.entry_codigo.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta beneficiario
        ttk.Label(
            frame_campos,
            text="ID beneficiario:"
        ).grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Caja texto beneficiario
        self.entry_beneficiario = ttk.Entry(frame_campos, width=30)

        self.entry_beneficiario.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta recurso
        ttk.Label(
            frame_campos,
            text="Código recurso:"
        ).grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Caja texto recurso
        self.entry_recurso = ttk.Entry(frame_campos, width=30)

        self.entry_recurso.grid(row=2, column=1, padx=10, pady=5)

        # Etiqueta cantidad
        ttk.Label(
            frame_campos,
            text="Cantidad:"
        ).grid(row=0, column=2, padx=10, pady=5, sticky="w")

        # Caja texto cantidad
        self.entry_cantidad = ttk.Entry(frame_campos, width=30)

        self.entry_cantidad.grid(row=0, column=3, padx=10, pady=5)

        # Etiqueta fecha
        ttk.Label(
            frame_campos,
            text="Fecha:"
        ).grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Caja texto fecha
        self.entry_fecha = ttk.Entry(frame_campos, width=30)

        self.entry_fecha.grid(row=1, column=3, padx=10, pady=5)

        # Etiqueta responsable
        ttk.Label(
            frame_campos,
            text="Responsable:"
        ).grid(row=2, column=2, padx=10, pady=5, sticky="w")

        # Caja texto responsable
        self.entry_responsable = ttk.Entry(frame_campos, width=30)

        self.entry_responsable.grid(row=2, column=3, padx=10, pady=5)

    #-------------------------------------------------------------------------------------
        # BOTONES
    #-------------------------------------------------------------------------------------

        # Frame para botones
        frame_botones = ttk.Frame(frame)

        frame_botones.pack(pady=10)

        # Botón registrar entrega
        ttk.Button(
            frame_botones,
            text="Registrar",
            command=self.registrar
        ).grid(row=0, column=0, padx=5)

        # Botón buscar por beneficiario
        ttk.Button(
            frame_botones,
            text="Buscar por beneficiario",
            command=self.buscar_beneficiario
        ).grid(row=0, column=1, padx=5)

        # Botón buscar por fecha
        ttk.Button(
            frame_botones,
            text="Buscar por fecha",
            command=self.buscar_fecha
        ).grid(row=0, column=2, padx=5)

        # Botón consultar todos
        ttk.Button(
            frame_botones,
            text="Consultar todos",
            command=self.consultar_todos
        ).grid(row=0, column=3, padx=5)

        # Botón limpiar campos
        ttk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar_campos
        ).grid(row=0, column=4, padx=5)

    #-------------------------------------------------------------------------------------
        # TABLA
    #-------------------------------------------------------------------------------------

        # Columnas tabla
        columnas = (
            "codigo",
            "beneficiario",
            "recurso",
            "cantidad",
            "fecha",
            "responsable",
            "valor"
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
        self.tree.heading("beneficiario", text="Beneficiario", anchor="center")
        self.tree.heading("recurso", text="Recurso", anchor="center")
        self.tree.heading("cantidad", text="Cantidad", anchor="center")
        self.tree.heading("fecha", text="Fecha", anchor="center")
        self.tree.heading("responsable", text="Responsable", anchor="center")
        self.tree.heading("valor", text="Valor", anchor="center")

        # Tamaño columnas
        self.tree.column("codigo", width=100, anchor="center")
        self.tree.column("beneficiario", width=130, anchor="center")
        self.tree.column("recurso", width=110, anchor="center")
        self.tree.column("cantidad", width=90, anchor="center")
        self.tree.column("fecha", width=110, anchor="center")
        self.tree.column("responsable", width=170, anchor="center")
        self.tree.column("valor", width=100, anchor="center")

#---------------------------------------------------------------------------------------------

    def limpiar_tabla(self):

        # Elimina filas tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

#---------------------------------------------------------------------------------------------

    def limpiar_campos(self):

        # Limpia las cajas de texto
        self.entry_codigo.delete(0, tk.END)
        self.entry_beneficiario.delete(0, tk.END)
        self.entry_recurso.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_responsable.delete(0, tk.END)

#---------------------------------------------------------------------------------------------

    def registrar(self):

        try:

            # Registra entrega
            self.controlador.registrar_entrega(
                self.entry_codigo.get(),
                self.entry_beneficiario.get(),
                self.entry_recurso.get(),
                self.entry_cantidad.get(),
                self.entry_fecha.get(),
                self.entry_responsable.get()
            )

            # Mensaje éxito
            messagebox.showinfo(
                "Éxito",
                "Entrega registrada correctamente!"
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
                    entrega.cantidad_entregada,
                    entrega.fecha,
                    entrega.responsable_entrega,
                    entrega.valor_economico
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

        # Verifica si hay resultados
        if len(lista) == 0:

            # Muestra mensaje si no hay resultados
            messagebox.showinfo(
                "Resultado",
                "No se encontraron entregas para ese beneficiario..."
            )

            return

        # Inserta resultados
        for entrega in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    entrega.codigo_entrega,
                    entrega.identificacion_beneficiario,
                    entrega.codigo_recurso,
                    entrega.cantidad_entregada,
                    entrega.fecha,
                    entrega.responsable_entrega,
                    entrega.valor_economico
                )
            )

#---------------------------------------------------------------------------------------------

    def buscar_fecha(self):

        # Limpia tabla
        self.limpiar_tabla()

        # Busca entregas fecha
        lista = self.controlador.listar_entregas_por_fecha(
            self.entry_fecha.get()
        )

        # Verifica si hay resultados
        if len(lista) == 0:

            # Muestra mensaje si no hay resultados
            messagebox.showinfo(
                "Resultado",
                "No se encontraron entregas en esa fecha..."
            )

            return

        # Inserta resultados
        for entrega in lista:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    entrega.codigo_entrega,
                    entrega.identificacion_beneficiario,
                    entrega.codigo_recurso,
                    entrega.cantidad_entregada,
                    entrega.fecha,
                    entrega.responsable_entrega,
                    entrega.valor_economico
                )
            )

#---------------------------------------------------------------------------------------------