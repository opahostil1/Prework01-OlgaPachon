'''
 Escribe un programa que convierta una temperatura de grados Celsius a grados 
Fahrenheit.
'''
def convertir (f):
  c = (f - 32) + 5/9
  return c
f = float (input('Poner Fahrenheit:'))
print (f'Pasar a Celsius: {convertir (f)}')