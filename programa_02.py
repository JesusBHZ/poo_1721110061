letra = input("Dime tu letra:")
a =[[0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,1,0,1,0]]

e =[[1,1,1,1,0],
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,1,0,0,0],
    [1,1,1,1,0]]

i =[[0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0]]

o =[[0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0]]

u =[[0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0]]

if letra == 'a':
  for i in range(len(a)):
    print(a[i])
elif letra == 'e':
  for i in range(len(e)):
    print(e[i])
elif letra == 'i':
  for ile in range(len(i)):
    print(i[ile])
elif letra == 'o':
  for i in range(len(o)):
    print(o[i])
elif letra == 'u':
  for i in range(len(u)):
    print(u[i])
else:
  print("Introduce una letra valida")