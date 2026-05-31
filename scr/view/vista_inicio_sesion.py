import tkinter as tk
from tkinter import ttk, messagebox

# Importa vista principal
from scr.view.vista_principal import VistaPrincipal

#---------------------------------------------------------------------------------------------

class VistaInicioSesion:

#---------------------------------------------------------------------------------------------

    def __init__(self, root, controlador):

        # Guarda controlador
        self.controlador = controlador

        # Guarda ventana raíz
        self.root = root

        # Crea ventana login
        self.window = tk.Toplevel(root)

        # Título ventana
        self.window.title("Inicio de Sesión")

        # Tamaño ventana
        self.window.geometry("480x320")

        # Evita redimensionar
        self.window.resizable(False, False)

        # Construye interfaz
        self._build_ui()

#---------------------------------------------------------------------------------------------

    def _build_ui(self):

        # Frame principal
        frame = ttk.Frame(self.window, padding=25)

        frame.pack(fill="both", expand=True)

        # Título principal
        ttk.Label(
            frame,
            text="Sistema Manos Solidarias",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        # Frame para datos de inicio de sesión
        frame_login = ttk.LabelFrame(
            frame,
            text="Datos de Acceso",
            padding=20
        )

        frame_login.pack(fill="x", pady=15)

        # Label usuario
        ttk.Label(
            frame_login,
            text="Usuario:"
        ).grid(row=0, column=0, padx=10, pady=8, sticky="w")

        # Entry usuario
        self.entry_usuario = ttk.Entry(frame_login, width=32)

        self.entry_usuario.grid(row=0, column=1, padx=10, pady=8)

        # Label contraseña
        ttk.Label(
            frame_login,
            text="Contraseña:"
        ).grid(row=1, column=0, padx=10, pady=8, sticky="w")

        # Entry contraseña
        self.entry_contrasena = ttk.Entry(
            frame_login,
            width=32,
            show="*"
        )

        self.entry_contrasena.grid(row=1, column=1, padx=10, pady=8)

        # Frame para botones
        frame_botones = ttk.Frame(frame)

        frame_botones.pack(pady=10)

        # Botón iniciar sesión
        ttk.Button(
            frame_botones,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        ).grid(row=0, column=0, padx=8)

        # Botón registrar usuario
        ttk.Button(
            frame_botones,
            text="Registrar usuario",
            command=self.registrar_usuario
        ).grid(row=0, column=1, padx=8)

#---------------------------------------------------------------------------------------------

    def limpiar_campos(self):

        # Limpia las cajas de texto
        self.entry_usuario.delete(0, tk.END)
        self.entry_contrasena.delete(0, tk.END)

#---------------------------------------------------------------------------------------------

    def iniciar_sesion(self):

        try:

            # Obtiene datos escritos
            usuario = self.entry_usuario.get()

            contrasena = self.entry_contrasena.get()

            # Valida credenciales
            valido = self.controlador.validar_inicio_sesion(
                usuario,
                contrasena
            )

            # Si login correcto
            if valido:

                messagebox.showinfo(
                    "Éxito",
                    "Inicio de sesión exitoso!"
                )

                # Cierra login
                self.window.destroy()

                # Abre menú principal
                VistaPrincipal(
                    self.root,
                    self.controlador
                )

        except ValueError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

#---------------------------------------------------------------------------------------------

    def registrar_usuario(self):

        try:

            # Obtiene datos escritos
            usuario = self.entry_usuario.get()

            contrasena = self.entry_contrasena.get()

            # Registra usuario
            self.controlador.registrar_usuario(
                usuario,
                contrasena
            )

            messagebox.showinfo(
                "Éxito",
                "Usuario registrado correctamente!"
            )

            # Limpia campos
            self.limpiar_campos()

        except ValueError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

#---------------------------------------------------------------------------------------------