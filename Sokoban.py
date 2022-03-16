class Sokoban:
  #Reprsentacion de comandos del juego
  #0 - Muñeco 
  #1 - Espacio  
  #2 - Cajas  
  #3 - Paredes  
  #4 - Metas  

 #Controles
  #a - Izquierda
  #d - Derecha  
  #w - Arriba  
  #w - Abajo  
  mapa = [3,1,1,1,0,1,1,1,3]#Define el mapa de juego
  posicion_x = 4 #Posicion inicial de personaje
  def __init__(self):
    pass

  def imprimirMapa(self): #Metodo para imprimir el mapa
    for i in self.mapa:#Recorre cada caracterer del juego
      if i == 1:#Si encuentra un numero 1 -  espacio
        print(" ", end = "")#Cambiar un 1 por un ""
      elif i == 3: #3-pared
        print(chr(190), end = "")#Cambia un 3 por un simbolo
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

