"""with open('archivo.txt', 'r') as f:
    lineas = [linea.split(") for linea in f]

for linea in   lineas:
print(linea)"""


import csv

with open('archivo.txt', 'r') as csvfile:
    rows = csv.reader(csvfile, delimiter='  ', quotechar='|')
  
    for row in rows:
      print(int (' '.join(row)))
    