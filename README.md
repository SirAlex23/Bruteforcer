# Bruteforcer

**Nota importante:** Este repositorio es un proyecto **educativo** que incluye **dos modos** para ilustrar técnicas de ataque contra contraseñas: **ataque por diccionario (wordlist)** y **fuerza bruta limitada**. Usa este código **solo** en entornos controlados (tu equipo, máquinas virtuales o laboratorios) y con autorización. El uso contra sistemas de terceros puede ser ilegal.
---

## Descripción
`BruteForcer` es un ejemplo didáctico en Python que permite:
- **Modo 1 — Diccionario:** prueba palabras de `diccionario.txt` y compara su hash SHA256 con un hash objetivo.
- **Modo 2 — Fuerza bruta (limitada):** genera combinaciones de caracteres hasta una longitud máxima configurable para ilustrar el concepto de brute-force.
- Ademas dispone de una demo en el archivo **index.html** que muestra el funcionamiento del proyecto.  

----

## Archivos principales
- `bruteforcer.py` — script principal (interactivo: elige modo 1 o 2).  
- `diccionario.txt` — ejemplo de wordlist (una palabra por línea).  
- `index.html` — página para GitHub Pages con documentación y acciones rápidas.  
- `README.md` — este archivo.

---

## Requisitos
- Python 3.8+  
(No requiere librerías externas en la versión base.)
- VS Code
- En el ataque por diccionario es importante tener el archivo `diccionario.txt` en la misma ruta que `bruteforcer.py`.

---

**Uso (entorno controlado)**  
1. Coloca `bruteforcer.py` y `diccionario.txt` en el mismo directorio.
 
2. Edita el archivo `bruteforcer.py` para cambiar `HASH_DE_PRUEBA` por el hash que quieras probar (solo en entornos de laboratorio).
   
3. Ejecuta:
   ```bash
   python3 bruteforcer.py

**Importante**: En el archivo **index.html** existe un zip descargable con todos los datos para que se pueda chequear que el proyecto funciona.
