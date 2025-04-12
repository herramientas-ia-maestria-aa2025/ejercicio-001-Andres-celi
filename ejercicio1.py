#Funcion para leer datos de un .txt y imprimirlos
#de manera clara. El separador en este caso es ;
with open("informacion.txt", 'r') as file:
    lineas = file.readlines()
    elementos = lineas.pop(0).split(';')
    print('Columnas:')
    for elemento in elementos:
        print(elemento)
    for linea in lineas:
        elementos_linea = linea.split(";")
        for n,valor in enumerate(elementos_linea):
            print(f'{elementos[n].strip()} : {valor}')

