class Sokoban:
  #Reprsentacion de comandos del juego------------
  #0 = muñeco
  #1 = espacio
  #2 = caja
  #3 = paredes
  #4 = metas
  #5 = muñeco_meta
  #6 = caja_meta

 #Controles------------
  #a - Izquierda
  #d - Derecha  
  #w - Arriba  
  #w - Abajo  
  
  #Avanzar (derecha)------------
#Cuando solo hay un muñeco
#0 - muñeco, especio -> [0,1] -> [1,0]
#1 - muñeco, meta -> [0,4] -> [1,5]
#2 - muñeco, caja, espacio ->  [0,2,1] -> [1,0,2]
#3 - muñeco, caja, meta -> [0,2,4] -> [1,0,6]

#Cuando hay un muñeco y una meta------------
#4 - muñeco_meta, espacio -> [5,1] -> [4,0]
#5 - muñeco_meta, meta -> [5,4] -> [4,5]
#6 - muñeco_meta, caja, espacio -> [5,2,1] -> [4,0,2]
#7 - muñeco_meta, caja, meta -> [5,2,4] -> [4,0,6]

#Faltan 4 sentencias más
#Ariba = -1
#Abajo = +1
#Derecha = +1
#Izquierda = -1
#-------------------------
#0 - muñeco, espacio
#pocision_x, posicion_x +1
#inicio -> [0, 1]
#termino -> [1,0]

# Una forma de hacerlo

#if #self.mapa [self.posicion_x +1]==1
   #self.mapa[self.posicion_x]=1
   #self.mapa[self.posicion_x + 1]=0
   #self.posicion_x +=1
#--------------------------
#if  
#elif

# solo son 1 condicion juntas

#if
#if
# son 2 condiciones cada una

#--------------------------------------------------
#[0,2,4] -> [1,0,6]
#0 = posicion_x
#2 = posicion_x+1
#4 = posicion_x+2


  mapa = [3,1,1,1,0,1,1,1,3]#Define el mapa de juego
  posicion_x = 4 #Posicion inicial de personaje
  def __init__(self):
    pass

  def imprimirMapa(self): #Metodo para imprimir el mapa
    for i in self.mapa:#Recorre cada caracterer del juego
      if i == 1:#Si encuentra un numero 1 -  espacio
        print(" ", end = "")#Cambiar un 1 por un ""
      elif i == 3: #3-pared
        print("|", end = "")#Cambia un 3 por un simbolo

        #print(chr(124), end = "")#Cambia un 3 por un simbolo |֍
      else:
        print(i, end=" ")
    print() #Imprime una linea vacia

  def moverDerecha(self): #Metddo para mover el personake a la derecha
    self.posicion_x +=1#Calcuala la nueva posicion del muñeco
    self.mapa[self.posicion_x] = 0#coloca el muñeco en la nueva posicion
    self.mapa[self.posicion_x - 1] = 1#coloca el espacio donde estaba el numero
  def moverIzquierda(self): #Metddo para mover el personake a la derecha
    self.posicion_x -=1#Calcuala la nueva posicion del muñeco
    self.mapa[self.posicion_x] = 0#coloca el muñeco en la nueva posicion
    self.mapa[self.posicion_x + 1] = 1#coloca el espacio donde estaba el numero

juego = Sokoban()#Crea un objeto para jugar
juego.imprimirMapa() #Imprime el mapa

while True:#Bucle para jugar N veces
  intrucciones = "d-Derecha\na-Izquierda"#Instrucciones
  print(intrucciones)
  movimientos = input("mover a: ")#Lee el movimiento
  if movimientos == 'd': #si es d - mover a la derecha
    juego.moverDerecha()#mueve el muñeco  a la derecha
    juego.imprimirMapa()#imprime el mapa
  elif movimientos == 'a': #si es a - mover a la izquierda
    juego.moverIzquierda()#mueve el muñeco  a la izquierda
    juego.imprimirMapa()#imprime el mapa
  elif movimientos == "q":#si es q-salir
    print("Saliste del juego")#Imprmir mesaje
    break #Rompe el ciclo while
