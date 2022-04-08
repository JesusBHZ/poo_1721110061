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



matriz = []
for i in range(m):
  matriz.append([])
  for j in range(n):
    for a in hola:
      matriz[i].append()
print(matriz)

