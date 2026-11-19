"""Punto de entrada del Sistema de Inventario (programa de consola).

Uso:
    python src/main.py             -> menú interactivo
    python src/main.py --verificar -> verificación rápida (para el despliegue)
"""
import sys

from producto import Producto

VERSION = "1.0.0"

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


def verificar():
    """Prueba de humo usada después de desplegar."""
    producto = Producto("P001", "Teclado", 350, 10)
    print(f"Sistema de Inventario v{VERSION} - verificación")
    print(producto.mostrar_informacion())
    print("VERIFICACION OK")


def menu():
    print(f"=== Sistema de Inventario v{VERSION} ===")
    while True:
        print("\n1. Registrar producto\n2. Mostrar productos\n3. Salir")
        try:
            opcion = input("Elige una opción: ").strip()
        except EOFError:
            break
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    if "--verificar" in sys.argv:
        verificar()
    else:
        menu()
