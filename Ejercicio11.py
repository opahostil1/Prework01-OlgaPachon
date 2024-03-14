'''
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad 
actual.
'''
def edad (año,nacimiento):
  edad=int(año-nacimiento)
  return edad
año= int(input("Introduce el año actual"))
nacimiento= int(input("Introduce el año de nacimiento"))
edadr=edad(año,nacimiento)
print (edadr)