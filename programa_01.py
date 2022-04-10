
"""fichero = open('archivo.txt', 'r')                  
hola = fichero.read()
texto=[]
for i in hola:
  texto+=i.rstrip()
print(texto)"""
import  numpy as np

archivo = open('archivo.txt', 'r')
hola = archivo.read()
# Columnas
with open("archivo.txt") as f:
    firstline = f.readline().rstrip()
n=len(firstline)
"""
columnas = archivo.readline()
n = len(archivo.readlines())
print(n)"""
#print(n)

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

"""
matriz = []
for i in range(n):
  matriz.append([])
  for a in texto:
    matriz[i][a].append(texto)
print(matriz)"""


np_array = np.array(texto, dtype=np.int64).reshape(m,n)
print(np_array)
print()
print(np_array[0,5])