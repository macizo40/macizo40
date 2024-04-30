cadena = input('Inserta tu nombre: ').lower()  # Convertir la cadena a minúsculas
contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in cadena:
    #lee todas las llaves sin necesidad de especificar posiciones
    if letra in contador_vocales:
        contador_vocales[letra] += 1

for vocal, contador in contador_vocales.items():
    print(f'La vocal {vocal} aparece {contador} veces')