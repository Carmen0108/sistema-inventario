# Sistema de Inventario

Programa de consola en **Python 3.12** que permite registrar y mostrar productos
(código, nombre, precio y existencia). Proyecto de las prácticas DevOps:
PLAN → CODE → **BUILD → TEST → RELEASE → DEPLOY**.

## Estructura
```
sistema-inventario/
├── src/
│   ├── producto.py        # Clase Producto
│   └── main.py            # Menú de consola (archivo principal)
├── tests/
│   └── test_producto.py   # Casos de prueba CP01–CP07 (unittest)
├── .github/workflows/
│   ├── build.yml          # BUILD: compila y verifica en cada push/PR
│   ├── test.yml           # TEST: ejecuta pruebas en cada push/PR
│   ├── release.yml        # RELEASE: publica versión al subir tag v*
│   └── deploy.yml         # DEPLOY: instala una versión en el servidor (SSH)
├── docs/DEPLOY.md         # Procedimiento de despliegue
└── CHANGELOG.md
```

## Ejecutar
```bash
python src/main.py              # menú interactivo
python src/main.py --verificar  # verificación rápida
```

## Pruebas
```bash
python -m unittest discover -s tests -v
```
