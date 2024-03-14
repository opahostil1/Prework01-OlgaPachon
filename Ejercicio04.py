'''
Crea un programa que cuente el número de vocales en una palabra ingresada por el 
usuario.
'''
texto = "Hola Mundo" 
vocales = "aeiouAEIOU" 
for letra in texto: 
  if letra in vocales: 
    print(letra)