'''
Crea un programa que cuente y muestre la cantidad de números pares e impares en 
una lista ingresada por el usuario.
'''

n = 1
par = impar = 0
while n != 0:
  n = int(input('Ingresa un numero: '))
  if n > 0:
    if n % 2 == 0:
      par += 1
    else:
      impar += 1
print('Cantidad de numeros pares: ', par)
print('Cantidad de numeros impares: ', impar)