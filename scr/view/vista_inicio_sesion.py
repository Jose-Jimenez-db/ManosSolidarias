import tkinter as tk
from tkinter import ttk, messagebox

# Importa vista principal
from view.vista_principal import VistaPrincipal

#---------------------------------------------------------------------------------------------

class VistaInicioSesion:

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
        self.window.geometry("450x300")

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
        ).grid(row=0, column=0, columnspan=2, pady=20)

        # Label usuario
        ttk.Label(
            frame,
            text="Usuario:"
        ).grid(row=1, column=0, padx=10, pady=10)

        # Entry usuario
        self.entry_usuario = ttk.Entry(frame, width=30)

        self.entry_usuario.grid(row=1, column=1)

        # Label contraseña
        ttk.Label(
            frame,
            text="Contraseña:"
        ).grid(row=2, column=0, padx=10, pady=10)

        # Entry contraseña
        self.entry_contrasena = ttk.Entry(
            frame,
            width=30,
            show="*"
        )

        self.entry_contrasena.grid(row=2, column=1)

        # Botón iniciar sesión
        ttk.Button(
            frame,
            text="Iniciar Sesión",
            command=self.iniciar_sesion
        ).grid(row=3, column=0, pady=20)

        # Botón registrar usuario
        ttk.Button(
            frame,
            text="Registrar Usuario",
            command=self.registrar_usuario
        ).grid(row=3, column=1)

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
                    "Inicio de sesión exitoso"
                )

                # Cierra login
                self.window.destroy()

                # Abre menú principal
                VistaPrincipal(
                    self.root,
                    self.controlador
                )

        except Exception as e:

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
                "Usuario registrado correctamente"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )