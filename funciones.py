

def suma(a,b):
    return a+b

def es_numero_valido(num=0):
    if num > 0:
        return True
    return False

#reciben y regresas dos valores ya modificados
def obtener_dos_valores(valor1,valor2):
    return valor1,valor2

def lenght_lista(lista):
    return len(lista)

def lenght_dict(diccio):
    return len(diccio)

def contador_de_vocales(cadena):
    contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in cadena:
    #lee todas las llaves sin necesidad de especificar posiciones
        if letra in contador_vocales:
            contador_vocales[letra] += 1
    return contador_vocales

resultado=es_numero_valido()
v1,v2=obtener_dos_valores(1,2)
print(resultado)
print(v1,v2)
print(lenght_lista([1,2]))


for vocal, contador in contador_de_vocales("la hora de la verdad").items():
    print(f'La vocal {vocal} aparece {contador} veces')