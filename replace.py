import re

# Función para realizar la sustitución de los exponentes
def reemplazar_exponentes(linea):

    patron_r_s_1 = r'([RS]t\d{1,2})\^4096'
    linea = re.sub(patron_r_s_1, r'\1b', linea)
    patron_r_s_2 = r'([RS]t\d{1,2})\^1024'
    linea = re.sub(patron_r_s_2, r'\1a', linea)

  
    patron_x_y = r'([XY]t\d{1,2})\^2'
    linea = re.sub(patron_x_y, r'\1b', linea)
    
    patron_h = r'(H\d{1,3})\^\d+'
    linea = re.sub(patron_h, r'\1', linea)
    
    return linea

def procesar_archivo(archivo_entrada, archivo_salida):
    try:
        # Abrir el archivo de entrada en modo lectura
        with open(archivo_entrada, 'r') as f_in:
            # Leer todas las líneas del archivo
            lineas = f_in.readlines()

        # Abrir el archivo de salida en modo escritura
        with open(archivo_salida, 'w') as f_out:
            # Procesar cada línea y escribir el resultado
            for linea in lineas:
                linea_procesada = reemplazar_exponentes(linea)
                f_out.write(linea_procesada)
        
        print(f"El archivo ha sido procesado y guardado como {archivo_salida}")
    
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_entrada} no se encuentra.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

# Llamada a la función principal
procesar_archivo('result.txt', 'result_replaced.txt')
