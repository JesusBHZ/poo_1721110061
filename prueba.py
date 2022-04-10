archivo = open('archivo.txt', 'r')
hola = archivo.read()
# Columnas
with open("archivo.txt") as f:
    firstline = f.readline().rstrip()
print(len(firstline))
#print(n)

#Filas
fichero = open('archivo.txt', 'r') 
fichero.readline()
fichero.seek(0)
m = len(fichero.readlines()) # devolvera 3


