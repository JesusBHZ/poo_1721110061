

import  numpy as np
nivel = 'archivo.txt'
archivo = open(nivel, 'r')
hola = archivo.read()
# Columnas
with open(nivel) as f:
    colum = f.readline().rstrip()
  
columnas = len(colum)


#Filas
fichero = open(nivel, 'r') 
fichero.readline()
fichero.seek(0)
m = len(fichero.readlines()) # devolvera 3


texto=[]
matriz = []

for i in hola:
  texto+=i.rstrip()
#print(texto)
for k in range(len(texto)):
    texto[k] = int(texto[k])

#print()
#print(texto)



np_array = np.array(texto).reshape(m,columnas)
#print(np_array)
#print()
#print(np_array[3,2])

result = np.where(np_array == 0)
rows, columns = np_array.shape
muneco_fila=result[0]
muneco_columna=result[1]
#print(muneco_fila)
#print(muneco_columna)
#print()
#print(m)
#print(columnas)
#print(rows)
#print(columns)

contador = 0
for r in hola:
  print(r)
  if r == 0:
    contador+=1
  else:
    pass
  if contador == 0:
    complete = True
  else:
    complete = False
  #return complete

print(complete)
    