#!/bin/bash
lista1=("a" "a" "a" "b" "b" "c" "d" "e") # Define la primera lista, lista1, con algunos elementos.
lista2=("pato" "pato" "pato" "mano" "mano" "perro" "gato" "jirafa") # Define la segunda lista, lista2, con algunos elementos.

len_lista1=${#lista1[@]} # Obtiene la longitud de la lista lista1 y la almacena en la variable len_lista1.
len_lista2=${#lista2[@]} # Obtiene la longitud de la lista lista2 y la almacena en la variable len_lista2.

if [[ $len_lista1 != $len_lista2 ]]; then # Comprueba si las longitudes de las dos listas son diferentes. Si son diferentes, imprime "Las listas no coinciden" y sale con un código de error 1.
    echo "Las listas no coinciden"
    exit 1
fi

# Se declaran dos arreglos asociativos (map1 y map2).
declare -A map1
declare -A map2

for ((i=1; i<=len_lista1; i++)); do # Itera sobre los índices de las listas usando un bucle for.
    key_list1=${lista1[$i]} # Obtiene el elemento actual de lista1 en la posición i y lo almacena en la variable key_list1.
    echo $key_list1
    if [[ ${map1[$key_list1]} != "" ]]; then # Comprueba si el elemento key_list1 ya existe en map1.
        if [[ ${lista2[$i]} != ${map1[$key_list1]} ]]; then
            echo "las listas no coinciden, $key_list1 ya existe y vale ${map1[$key_list1]}, no ${lista2[$i]}"
            exit 1
        fi
    else # key_list1 no existe en map1
        key_list2=${lista2[$i]}

        if [[ ${map2[$key_list2]} != "" ]]; then # verifica si el elemento correspondiente en lista2 ya está mapeado en map2.
            echo "las listas no coinciden, $key_list2 ya existe y vale ${map2[$key_list2]}, no $key_list1"
            exit 1
        fi
        # Se registran las llaves y los valores unicos en cada mapa, e.g.
        # map1 {
        #     "a": "pato"
        # }
        # map2 {
        #     "pato": "a"
        # }
        map1[$key_list1]=$key_list2
        map2[$key_list2]=$key_list1
    fi
done

echo "las listas coinciden" # Si no hay problemas, imprime "Las listas coinciden".