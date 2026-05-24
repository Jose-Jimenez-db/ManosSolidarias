import json
import os
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

class Repositorio(Generic[T]):
    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo
        self._asegurar_archivo()

    def _asegurar_archivo(self):
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w') as f:
                json.dump([], f)

    def cargar_todos(self) -> List[dict]:
        with open(self.ruta_archivo, 'r') as f:
            return json.load(f)

    def guardar_todos(self, datos: List[dict]):
        with open(self.ruta_archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def agregar(self, dato: dict):
        datos = self.cargar_todos()
        datos.append(dato)
        self.guardar_todos(datos)

    def buscar_por_campo(self, campo: str, valor) -> Optional[dict]:
        datos = self.cargar_todos()
        for dato in datos:
            if dato[campo] == valor:
                return dato
        return None

    def eliminar_por_campo(self, campo: str, valor):
        datos = self.cargar_todos()
        datos = [d for d in datos if d[campo] != valor]
        self.guardar_todos(datos)

    def actualizar(self, campo: str, valor, nuevo_dato: dict):
        datos = self.cargar_todos()
        for i, dato in enumerate(datos):
            if dato[campo] == valor:
                datos[i] = nuevo_dato
                break
        self.guardar_todos(datos)