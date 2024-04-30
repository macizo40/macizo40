#introducir una cadena y crear una funcion que me regrese un diccionario con sus letras y el numero de veces que se repiten
cadena = input('Inserta la cadena: ')  # Convertir la cadena a minúsculas
#creo el diccionario de la cadena asignandole a todas las llaves el valor de 0, las llaves no se repiten


def contar_letras(cadena):
    letras = dict.fromkeys(cadena, 0)
    for letra in cadena:
        #lee todas las llaves sin necesidad de especificar posiciones tomando lo mismo que las vocales
        if letra in letras:
            letras[letra] += 1
    return letras

letras = contar_letras(cadena)

#recorro todos los elementos agregandole un contador
for elemento, contador in letras.items():
    print(f'La letra {elemento} aparece {contador} veces')
