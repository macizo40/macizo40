#data types 
cadenas = 'this is an string'
entero = 1
real = .1
listas = ['uno',1,1.0]
diccionario = {'llave1':'valor1'}
bandera = True
bandera2 = False
puntero = None

#iterar indices
for i in range(0,len(listas)):
    print(f'{listas[i]}')

#iterar elementos aka for each, strings listas, datos iterables
for item in listas:
    print(f'{item}')


#iterar mapas
for key in diccionario:
    print(f'{key}')
    print(f'{diccionario[key]}')

#iterar llaves
for key in diccionario.keys():
    print(f'{key}')

#iterar valores
for value in diccionario.values():
    print(f'{value}')

#condiciones
if 1 in listas:
    print('estoy dentro')

#seleccion canonica todos los if apilados para diferentes acciones
if listas[0] == 'one':
    print('el valor es one')
elif listas[0] == 'uno':
    print('el valor es uno')
else:
    print('no es ningun valor')

#agregar valores a un diccionario 
diccionario['llave2'] = 'valor2'
