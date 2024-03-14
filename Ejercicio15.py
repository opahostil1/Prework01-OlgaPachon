'''
 Escribe un programa que convierta un número de minutos en horas y minutos. Por 
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''
minuto = int(input('Ingresa los minutos:'))
hora = minuto //60
minutos = minuto %60
print('hora:', hora, 'minutos:', minutos)