# Procedimiento de despliegue — Sistema de Inventario

## 1. Requisitos del entorno de destino
| Requisito | Valor |
|---|---|
| Sistema operativo | Linux (Ubuntu 22.04/24.04) o Windows/macOS para despliegue manual |
| Python | 3.10 o superior (`python3 --version`) |
| Herramientas | `unzip`, servidor SSH (`openssh-server`) para despliegue automático |
| Dependencias externas | Ninguna (solo biblioteca estándar) |
| Espacio | < 1 MB por versión |

## 2. Versión a instalar
Se toma de **GitHub → Releases** (ej. `v1.0.0`, archivo `sistema-inventario-v1.0.0.zip`).
No se vuelve a generar el paquete: se usa el artefacto publicado en la fase RELEASE.

## 3. Despliegue manual
```bash
mkdir despliegue-inventario && cd despliegue-inventario
# descargar sistema-inventario-v1.0.0.zip desde Releases y guardarlo aquí
unzip sistema-inventario-v1.0.0.zip -d version-v1.0.0
cd version-v1.0.0
python3 src/main.py --verificar     # debe imprimir VERIFICACION OK
python3 src/main.py                 # registrar y mostrar un producto
```
En Windows: extraer con clic derecho → *Extraer todo* y usar `python` en lugar de `python3`.

## 4. Configuración
No requiere archivos de configuración ni variables de entorno.
Para el despliegue automático se configuran los secretos del repositorio:
`DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY`, `DEPLOY_PORT`.

## 5. Despliegue automático (GitHub Actions)
Actions → **Despliegue del Sistema de Inventario** → *Run workflow* → escribir la versión (ej. `v1.0.0`).
El workflow descarga el ZIP del Release, lo copia por SCP al servidor, lo extrae en
`~/sistema-inventario/version-<tag>/`, ejecuta `--verificar` y actualiza el enlace
`~/sistema-inventario/actual` para que apunte a la versión instalada.

## 6. Comprobar que funciona
```bash
ssh usuario@servidor
cd ~/sistema-inventario/actual
python3 src/main.py
```
Registrar un producto (opción 1) y mostrarlo (opción 2).

## 7. Recuperar la versión anterior (rollback)
Opción A — volver a ejecutar el workflow de despliegue con la versión anterior (ej. `v1.0.0`).
Opción B — directo en el servidor:
```bash
cd ~/sistema-inventario
ln -sfn version-v1.0.0 actual
python3 actual/src/main.py --verificar
```
Las versiones anteriores se conservan en su propia carpeta, por eso el regreso es inmediato.

## 8. Problemas frecuentes
| Problema | Causa | Solución |
|---|---|---|
| `python3: command not found` | Python no instalado | `sudo apt install python3` |
| `unzip: command not found` | Falta unzip | `sudo apt install unzip` |
| `ModuleNotFoundError: producto` | Se ejecutó desde otra carpeta o faltan archivos | Ejecutar `python3 src/main.py` dentro de la carpeta de la versión |
| Workflow: `Permission denied (publickey)` | Llave SSH incorrecta o no autorizada | Revisar `DEPLOY_KEY` y `~/.ssh/authorized_keys` del servidor |
| Workflow: `dial tcp ... i/o timeout` | Servidor no accesible desde Internet / puerto cerrado | Revisar IP pública y que el puerto 22 esté abierto |
| Release downloader: `not found` | La etiqueta no existe o no tiene ZIP | Verificar el tag en Releases |
