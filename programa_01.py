

import  numpy as np

archivo = open('archivo.txt', 'r')
hola = archivo.read()
# Columnas

with open("archivo.txt") as f:
    firstline = f.readline().rstrip()
n=len(firstline)


#Filas
fichero = open('archivo.txt', 'r') 
fichero.readline()
fichero.seek(0)
m = len(fichero.readlines()) # devolvera 3



fichero = open('archivo.txt', 'r') 
hola = fichero.read()
texto=[]
matriz = []

for i in hola:
  texto+=i.rstrip()
print(texto)
for k in range(len(texto)):
    texto[k] = int(texto[k])

print()
print(texto)



np_array = np.array(texto).reshape(m,n)
print(np_array)
print()
print(np_array[3,2])

result = np.where(np_array == 0)
rows, columns = np_array.shape
muneco_fila=result[0]
muneco_columna=result[1]
print()
print(muneco_fila)
print(muneco_columna)