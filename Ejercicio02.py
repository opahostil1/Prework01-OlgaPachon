'''
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo 
una propina del 15% sobre el total de la cuenta.
'''
comida = 50
impuesto = 0.21
propina = 0.15

comida = comida + comida * impuesto
total = comida + comida * propina
print ('%2f'%total)