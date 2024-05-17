# Almacenar la lista de nombres de alumnos, por cada
# alumno un listado de notas de todo el ciclo
import os

def solicitar_datos_generales():
    n_alumnos = 0
    n_notas = 0
    while True:
        os.system('cls')
        n_alumnos =  int(input('Ingrese la cantidad de alumnos: '))
        n_notas = int(input('Ingrese la cantidad de notas por alumno: '))
        if n_alumnos > 0 and n_notas > 0:
            return n_alumnos, n_notas
        else: 
            print('\nValores no soportados')
            os.system('pause')

def solicitar_datos_alumno():
    nombre = input("Nombre del alumno: ")
    apellido = input("Apellido del alumno: ")
    seccion = input("Sección del alumno: ")
    grado = input("Grado del alumno: ")
    print()
    return nombre, apellido, seccion, grado

# + Funcion de promedio de notas
def hallar_promedio(notas):
    return sum(notas) / len(notas)

# + Funcion de alumno con mayor promedio
def obtener_alumno_promedio(nombres, promedios):
    promedio_mayor = 0
    for promedio in promedios:
        if promedio_mayor < promedio:
            promedio_mayor = promedio

    indice_promedio = promedios.index(promedio_mayor)
    return nombres[indice_promedio]

# + Validaciones (notas >0 <20, el valor de la
# nota no pertenece a un rango válido)
def validacion_notas(nota):
    if 0 <= nota and nota <= 20:
        return True
    else:
        print('El valor de la nota no pertenece a un rango válido')
        return False

# + Nombre del alumno con mayor promedio en UPPER()
def validacion_mayusculas(nombre):
    return nombre.isupper()

# + Almacenar los elementos en listas
lista_nombres = []
lista_notas = []
# + Solicitar la cantidad
# + Solicitar la cantidad de notas por cada alumno
n_alumnos, n_notas = solicitar_datos_generales()

# + Solicitar los datos de cada alumno
print('----------------------------------')
print('\n SOLICITANDO DATOS DE ALUMNOS \n')
print('----------------------------------')
for i in range(n_alumnos):
    print('+------------------+')
    print(f'| ALUMNO N° {i + 1}    |')
    print('+------------------+')
    nombre, apellido,_,_, = solicitar_datos_alumno()
    notas = []
    for j in range(n_notas):
        while True:
            try:
                nota = float(input(f'Nota {j + 1} : '))
                if (validacion_notas(nota)): 
                    notas.append(nota)
                    break
            except:
                print('Error: Por favor ingrese un número valido')    
    
    lista_nombres.append(nombre + ' ' + apellido)
    lista_notas.append(notas)

promedios = [hallar_promedio(notas) for notas in lista_notas]
nombre_mayor_promedio = obtener_alumno_promedio(lista_nombres, promedios)

if not validacion_mayusculas(nombre_mayor_promedio):
    indice_nombre = lista_nombres.index(nombre_mayor_promedio)
    lista_nombres[indice_nombre] = lista_nombres[indice_nombre].upper()

print('\nPromedio de notas por alumno\n')
for nombre, promedio in zip(lista_nombres, promedios):
    print(f'{nombre}: {promedio}')
