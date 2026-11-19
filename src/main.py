"""Punto de entrada del Sistema de Inventario (programa de consola).

VERSIÓN v1.1.0 — agrega "Buscar producto".
OJO: trae un ERROR INTENCIONAL para la práctica DEPLOY (simular falla y regresar a v1.0.0).
Las pruebas unitarias pasan (solo prueban Producto), por eso sí se libera,
pero al usar la opción 3 en el servidor el programa truena.
"""
import sys

from producto import Producto

VERSION = "1.1.0"

inventario = []


def registrar_producto():
    print("\n--- Registrar producto ---")
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    try:
        precio = float(input("Precio: "))
        existencia = int(input("Existencia: "))
    except ValueError:
        print("Error: el precio debe ser numérico y la existencia un entero.")
        return
    inventario.append(Producto(codigo, nombre, precio, existencia))
    print("Producto registrado correctamente.")


def mostrar_productos():
    print("\n--- Productos registrados ---")
    if not inventario:
        print("No hay productos registrados.")
        return
    for producto in inventario:
        print(producto.mostrar_informacion())
        print("-" * 25)


def buscar_producto():
    print("\n--- Buscar producto ---")
    codigo = input("Código a buscar: ").strip()
    for producto in inventario:
        if producto.obtener_codigo() == codigo:
            # ERROR INTENCIONAL: el método mostrar_resumen() no existe
            print(producto.mostrar_resumen())
            return
    print("Producto no encontrado.")


def verificar():
    """Prueba de humo usada después de desplegar."""
    producto = Producto("P001", "Teclado", 350, 10)
    print(f"Sistema de Inventario v{VERSION} - verificación")
    print(producto.mostrar_informacion())
    print("VERIFICACION OK")


def menu():
    print(f"=== Sistema de Inventario v{VERSION} ===")
    while True:
        print("\n1. Registrar producto\n2. Mostrar productos\n3. Buscar producto\n4. Salir")
        try:
            opcion = input("Elige una opción: ").strip()
        except EOFError:
            break
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    if "--verificar" in sys.argv:
        verificar()
    else:
        menu()
