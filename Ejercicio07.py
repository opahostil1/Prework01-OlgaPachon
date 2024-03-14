'''
 Crea un programa que realice operaciones aritméticas simples (suma, resta, 
multiplicación, división) según la elección del usuario.
'''
numero1 = int(input("Introduzca el primer numero:"))
numero2 = int(input("Introduzca el segundo numero:"))

eleccion = 0

while eleccion != 5:
  print('''
  Seleccione operacion:
  1) sumar
  2) restar
  3) multiplicar
  4) dividir
  5) salir
  ''')
  eleccion = int(input())
  if eleccion == 1:
    print(" ")
    print ("Total: ",numero1," + ", numero2, " =", numero1+numero2)
  elif eleccion ==2:
    print(" ")
    print ("Total: ",numero1," - ", numero2, " =", numero1-numero2)
  elif eleccion ==3:
    print(" ")
    print ("Total: ",numero1," * ", numero2, " =", numero1*numero2)
  elif eleccion ==4:
    print(" ")
    print ("Total: ",numero1," / ", numero2, " =", float(numero1/numero2))
  elif eleccion ==5:
    print ("Gracias")
    