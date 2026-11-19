"""Modelo Producto del Sistema de Inventario."""


class Producto:
    """Representa un producto del inventario."""

    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def obtener_codigo(self):
        return self.codigo

    def obtener_nombre(self):
        return self.nombre

    def obtener_precio(self):
        return self.precio

    def obtener_existencia(self):
        return self.existencia

    def mostrar_informacion(self):
        """Regresa (y permite imprimir) toda la información del producto."""
        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: {self.precio}\n"
            f"Existencia: {self.existencia}"
        )

    def __str__(self):
        return self.mostrar_informacion()
