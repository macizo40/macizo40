#programa que cuente cuantas vocales hay en una cadena

cadena = input('inserta tu nombre: ')
edad = int(input('ingresa tu edad: '))
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letra in cadena:
    if letra == 'a' or letra == 'A':
        contador_a += 1
    elif letra == 'e' or letra == 'E':
        contador_e += 1
    elif letra == 'i' or letra == 'I':
        contador_i += 1
    elif letra == 'o' or letra == 'O':
        contador_o += 1
    elif letra == 'u' or letra == 'U':
        contador_u += 1
    elif letra == ' ':
        pass
    else:
        print(f'{letra} no es una vocal')

print(f' la volcal a aparece {contador_a} veces')
print(f' la volcal e aparece {contador_e} veces')
print(f' la volcal i aparece {contador_i} veces')
print(f' la volcal o aparece {contador_o} veces')
print(f' la volcal u aparece {contador_u} veces')