"""
with open('archivo.txt', 'r') as f:
    lineas = [linea.split(") for linea in f]

for linea in   lineas:
print(linea)¿


import csv

with open('archivo.txt', 'r') as csvfile:
    rows = csv.reader(csvfile, delimiter='  ', quotechar='|')
  
    for row in rows:
      print(int (' '.join(row)))


      # archivo-entrada.py
f = open ('archivo.txt','r')
#mensaje = f.read().split("\n")
#mensaje = f.read()
print(mensaje)


for i in mensaje:
  print(i)

import numpy 
archivo = open('archivo.txt', 'r')
lista = []
cont = 0
for linea in archivo.read():
  cont+=1
  lista.append(linea)
archivo.close()

def separar_lineas(lista):
  lista_num = []
  for indice, l in enumerate(lista):
    lista_num.append(lista[indice].split("\n"))
  return lista_num
lista = separar_lineas(lista)

print(lista)


import numpy as np

with open('archivo.txt','r') as f:
    datos = ','.join(f.readlines()).replace('\n',';').delimiter=','

m = np.matrix(datos)
print(m[0][0])


import numpy 
archivo = open('archivo.txt', 'r')
lista = []
cont = 0
for linea in archivo.read():
  cont+=1
  lista.append(linea)
archivo.close()

def separar_lineas(lista):
  lista_num = []
  for indice, l in enumerate(lista):
    lista_num.append(lista[indice].split("\n"))
  return lista_num
lista = separar_lineas(lista)

print(lista)


import csv

with open("archivo.txt") as f:
    line = csv.reader(f, delimiter=',')
print(line)"""

import numpy 
archivo = open('archivo.txt', 'r')
arreglo = []
cont = 0
for linea in archivo.read():
  cont+=1
  lista.append(linea)
archivo.close()

def separar_lineas(lista):
  lista_num = []
  for indice, l in enumerate(lista):
    lista_num.append(lista[indice].split("\n"))
  return lista_num
lista = separar_lineas(lista)

print(lista)
#################################
archivo = open('archivo.txt', 'r')
matriz = []
n = fichero.readline()
for i in range(n):
    matriz.append([])
    for j in range(m):

print(matriz)


fichero = open('texto5_8.txt', 'r')
texto_completo = fichero.read()
caracteres = len(texto_completo)




Counter = 0
  
Content = file.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1