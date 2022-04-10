a = 'archivo.txt'
archivo = open(a, 'r')
hola = archivo.read()
# Columnas
with open(a) as f:
    firstline = f.readline().rstrip()
print(len(firstline))
#print(n)

#Filas
fichero = open(a, 'r') 
fichero.readline()
fichero.seek(0)
m = len(fichero.readlines())
print(m)# devolvera 3


