'''
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
def imc(estatura,peso):
  return peso / estatura**2

peso = float(input('Escriba su peso (Kg):'))
estatura = float(input('Escriba su estatura (m):'))

indice = imc (estatura,peso)

print ('Su imc es: {}'.format(indice))