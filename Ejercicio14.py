'''
 Crea un programa que calcule el precio final de un artículo después de aplicar un 
descuento del 20%.
'''
precio = float(input('Ingresa el precio:'))
descuento = precio * 0.20
precio_final = precio - descuento

print(f'El precio final con descuento es de ${precio_final: .2f}')