"""Pruebas de la funcionalidad Producto (fase TEST)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from producto import Producto  # noqa: E402


class TestProducto(unittest.TestCase):

    def setUp(self):
        self.producto = Producto("P001", "Teclado", 350, 10)

    def test_cp01_crear_producto(self):
        """CP01 - Crear producto"""
        self.assertIsInstance(self.producto, Producto)

    def test_cp02_mostrar_codigo(self):
        """CP02 - Mostrar código"""
        self.assertEqual(self.producto.obtener_codigo(), "P001")

    def test_cp03_mostrar_nombre(self):
        """CP03 - Mostrar nombre"""
        self.assertEqual(self.producto.obtener_nombre(), "Teclado")

    def test_cp04_mostrar_precio(self):
        """CP04 - Mostrar precio"""
        self.assertEqual(self.producto.obtener_precio(), 350)

    def test_cp05_mostrar_existencia(self):
        """CP05 - Mostrar existencia"""
        self.assertEqual(self.producto.obtener_existencia(), 10)

    def test_cp06_mostrar_informacion_completa(self):
        """CP06 - Mostrar información completa"""
        info = self.producto.mostrar_informacion()
        for dato in ("P001", "Teclado", "350", "10"):
            self.assertIn(dato, info)

    def test_cp07_crear_segundo_producto(self):
        """CP07 - Crear segundo producto"""
        mouse = Producto("P002", "Mouse", 180, 5)
        self.assertEqual(mouse.obtener_codigo(), "P002")
        self.assertEqual(mouse.obtener_nombre(), "Mouse")
        self.assertEqual(mouse.obtener_precio(), 180)
        self.assertEqual(mouse.obtener_existencia(), 5)
        # el primero no debe cambiar
        self.assertEqual(self.producto.obtener_nombre(), "Teclado")


if __name__ == "__main__":
    unittest.main(verbosity=2)
