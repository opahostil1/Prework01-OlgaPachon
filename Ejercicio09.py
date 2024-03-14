'''
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 
1 dólar es igual a 0.85 euros.
'''
dolar = 0.85
while True :
  euros = float (input("Ingresa los euros"))
  dolares = euros / dolar
  print ("{} euros equivalentes a {} dolares" .format (euros,dolares))