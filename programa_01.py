
"""fichero = open('archivo.txt', 'r')                  
hola = fichero.read()
texto=[]
for i in hola:
  texto+=i.rstrip()
print(texto)"""

archivo = open('archivo.txt', 'r')
hola = archivo.read()
# Columnas
columnas = archivo.readline()
n = len(columnas)
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




matriz = []
for i in range(n):
  matriz.append([])
  for a in texto:
    matriz[i][a].append(texto)
print(matriz)