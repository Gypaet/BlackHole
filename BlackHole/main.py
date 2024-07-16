import os
import secrets

from title import title

print(title)

# Solicita el número de pasadas para la sobreescritura del archivo

def solicitar_pasadas():
    
    while True:
        try:
            
            pasadas = int(input(" >>> [:] Ingrese el número de pasadas de sobreescritura: "))
            
            if 3 <= pasadas <= 50:
                return pasadas
            else:
                print("Por favor, ingrese un número entero entre 3 y 50.")
                
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            
    return pasadas

# Solicita la ruta del archivo que debe ser eliminado
    
ruta_archivo = input(' >>> [:] Introduzca la ruta del archivo que desea eliminar: ')

# Línea 31 - línea 38, el programa verifica que los datos introducidos por el usuario sean válidos y coherentes

while not os.path.exists(ruta_archivo):
    
    print('\n [!] No se ha podido encontrar la ruta especificada\n Por favor, introduzca una ruta correcta\n')
    ruta_archivo = input(' >>> [:] Introduzca la ruta del archivo que desea eliminar: ')
    
tamano_archivo = os.path.getsize(ruta_archivo)

pasadas = solicitar_pasadas()

print(''' >>> [!] BlackHole eliminará de forma irrecuperable el archivo seleccionado.
                  Asegúrese de que el archivo seleccionado realmente debe ser eliminado
''')

advertencia = input(' >>> Introduzca 1 para continuar, 0 para cancelar: ')

if advertencia == '1':
    
    # Proceso de eliminación del archivo
    # Sobreescritura de datos

    with open(ruta_archivo, "r+b") as f:
        
        for i in range(pasadas):
            
            print(f"Pass {i + 1} of {pasadas}")
            datos_aleatorios = secrets.token_bytes(tamano_archivo)

            f.seek(0)
            f.write(datos_aleatorios)
            f.flush()
            os.fsync(f.fileno())
            
            f.write(b'\x00' * tamano_archivo)
            
            os.remove(ruta_archivo)
            
    print('Operación completada')
                    
else:
    
    # Proceso de eliminación de archivo cancelado, cierre del programa
    
    print(' >>> [:] La operación ha sido cancelada')
    input(' >>> Pulse ENTER para cerrar el programa: ')