'''
 Escribe un programa que determine si un año ingresado por el usuario es bisiesto o 
no.
'''
def bisiesto(año):
  if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    return 'El año %d es bisiesto.' % año
  else:
    return 'El año %d no es bisiesto.' % año
  
try:
  año = int(input('Dame un año:'))
  print(bisiesto(año))
except:
  print('Valor erroneo')