import hashlib
import time
import sys
import itertools
import string

# =============================================================
# 1. CONFIGURACIÓN INICIAL Y HASHES OBJETIVO
# =============================================================

# HASH PARA MODO 1 (Diccionario): Hash SHA256 de la palabra 'miclave' (Hash VERIFICADO)
HASH_DICCIONARIO = '08a417d732e03b18797c81e6f9befd5ef3632f162c5b920e2bec64e89a2dce33' 
ARCHIVO_DE_DICCIONARIO = 'diccionario.txt' 

# HASH PARA MODO 2 (Fuerza Bruta Pura): Hash SHA256 de la contraseña CORTA 'a1' (TU HASH CORRECTO)
HASH_FUERZA_BRUTA = 'f55ff16f66f43360266b95db6f8fec01d76031054306ae4a4b380598f6cfd114' 

# Configuraciones para el MODO FUERZA BRUTA PURA:
CARACTERES_PRUEBA = string.ascii_lowercase + string.digits  
LONGITUD_MAXIMA = 4  


# =============================================================
# MODO 1: ATAQUE DE DICCIONARIO
# =============================================================
def crackear_diccionario(hash_objetivo, archivo_diccionario):
    
    print(f"\n[*] Iniciando ataque de DICCIONARIO SHA256...")
    print(f"[*] Hash Objetivo: {hash_objetivo}")
    
    try:
        # Abre el archivo de diccionario y fuerza la codificación UTF-8
        with open(archivo_diccionario, 'r', encoding='utf-8') as f:
            # Lee cada línea, elimina espacios en blanco al inicio/fin
            palabras = [linea.strip() for linea in f]
    except FileNotFoundError:
        print(f"[!] ERROR: Archivo '{archivo_diccionario}' no encontrado. Verifica la ruta.")
        return

    inicio_tiempo = time.time()
    
    for i, palabra in enumerate(palabras):
        
        # Generar el Hash de la Palabra de Prueba
        hash_generado = hashlib.sha256(palabra.encode('utf-8')).hexdigest()

        if hash_generado == hash_objetivo:
            
            fin_tiempo = time.time()
            tiempo_total = fin_tiempo - inicio_tiempo
            
            print(f"\n[+] ¡ÉXITO! Contraseña encontrada:")
            print(f"[+] Contraseña Original: {palabra}")
            print(f"[+] Intentos realizados: {i + 1}")
            print(f"[+] Tiempo Total: {tiempo_total:.4f} segundos")
            return

    fin_tiempo = time.time()
    tiempo_total = fin_tiempo - inicio_tiempo
    print(f"\n[-] FRACASO: Contraseña no encontrada en el diccionario.")
    print(f"[-] Intentos totales: {len(palabras)}")
    print(f"[-] Tiempo Total: {tiempo_total:.2f} segundos")


# =============================================================
# MODO 2: FUERZA BRUTA PURA
# =============================================================
def crackear_fuerza_bruta_pura(hash_objetivo, caracteres, longitud_max):
    
    print(f"\n[*] Iniciando ataque de FUERZA BRUTA PURA...")
    print(f"[*] Probando combinaciones de {len(caracteres)} caracteres hasta longitud {longitud_max}.")
    inicio_tiempo = time.time()
    
    for longitud in range(1, longitud_max + 1):
        print(f"[*] Probando contraseñas de longitud: {longitud}...")
        
        for intento in itertools.product(caracteres, repeat=longitud):
            
            palabra = "".join(intento)
            hash_generado = hashlib.sha256(palabra.encode('utf-8')).hexdigest()
            
            if hash_generado == hash_objetivo:
                
                fin_tiempo = time.time()
                tiempo_total = fin_tiempo - inicio_tiempo
                
                print(f"\n[+] ¡ÉXITO! Contraseña encontrada!")
                print(f"[+] Contraseña Original: {palabra}")
                print(f"[+] Tiempo Total: {tiempo_total:.4f} segundos")
                return
    
    print("\n[-] FRACASO: Contraseña no encontrada en el rango definido.")


# =============================================================
# 5. PUNTO DE ENTRADA DEL PROGRAMA
# =============================================================
if __name__ == "__main__":
    
    print("\n--- Analizador de Seguridad de Contraseñas ---")
    print("1: Ataque de Diccionario (Objetivo: 'miclave')")
    print(f"2: Fuerza Bruta Pura (Objetivo: 'a1' - Max. Longitud {LONGITUD_MAXIMA})")
    
    modo = input("Elige el modo (1/2): ")

    if modo == '1':
        crackear_diccionario(HASH_DICCIONARIO, ARCHIVO_DE_DICCIONARIO)
        
    elif modo == '2':
        crackear_fuerza_bruta_pura(HASH_FUERZA_BRUTA, CARACTERES_PRUEBA, LONGITUD_MAXIMA)
        
    else:
        print("[!] Modo no válido. Saliendo.")