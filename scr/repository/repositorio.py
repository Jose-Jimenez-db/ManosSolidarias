import json
import os
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

#---------------------------------------------------------------------------------------------

class Repositorio(Generic[T]):
    """Gestiona las operaciones de almacenamiento de datos en archivos JSON."""

#---------------------------------------------------------------------------------------------

    def __init__(self, ruta_archivo: str):
        """Inicializa el repositorio y verifica la existencia del archivo."""
        self.ruta_archivo = ruta_archivo
        self._asegurar_archivo()

#---------------------------------------------------------------------------------------------

    def _asegurar_archivo(self):
        """Crea el archivo JSON si todavía no existe."""
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w') as f:
                json.dump([], f)

#---------------------------------------------------------------------------------------------

    def cargar_todos(self) -> List[dict]:
        """Obtiene todos los registros almacenados en el archivo."""
        with open(self.ruta_archivo, 'r') as f:
            return json.load(f)

#---------------------------------------------------------------------------------------------

    def guardar_todos(self, datos: List[dict]):
        """Guarda la lista completa de registros en el archivo."""
        with open(self.ruta_archivo, 'w') as f:
            json.dump(datos, f, indent=4)

#---------------------------------------------------------------------------------------------

    def agregar(self, dato: dict):
        """Agrega un nuevo registro al archivo de almacenamiento."""
        datos = self.cargar_todos()
        datos.append(dato)
        self.guardar_todos(datos)

#---------------------------------------------------------------------------------------------

    def buscar_por_campo(self, campo: str, valor) -> Optional[dict]:
        """Busca un registro utilizando el valor de un campo específico."""
        datos = self.cargar_todos()
        for dato in datos:
            if dato[campo] == valor:
                return dato
        return None

#---------------------------------------------------------------------------------------------

    def eliminar_por_campo(self, campo: str, valor):
        """Elimina los registros que coincidan con el valor indicado."""
        datos = self.cargar_todos()
        datos = [d for d in datos if d[campo] != valor]
        self.guardar_todos(datos)

#---------------------------------------------------------------------------------------------

    def actualizar(self, campo: str, valor, nuevo_dato: dict):
        """Actualiza un registro existente con nueva información."""
        datos = self.cargar_todos()
        for i, dato in enumerate(datos):
            if dato[campo] == valor:
                datos[i] = nuevo_dato
                break
        self.guardar_todos(datos)

#---------------------------------------------------------------------------------------------