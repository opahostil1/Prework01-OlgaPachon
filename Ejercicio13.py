'''
Escribe un programa que determine si un número ingresado por el usuario es primo 
o no
'''

n = int(input('Escribe un numero:'))
x = 1
c = 0
while x <= n:
  if n%x==0:
    c = c+1
  x = x+1
if c ==2:
  print('Numero', n, 'primo')
else:
  print('Numero', n, 'no primo')