#!/bin/bash
# Teniendo dos cadenas donde una tiene "a,a,a,b,b,c,d,e" y otra cadena tiene "pato, pato, pato, mano, mano, perro, gato, jirafa" como comparar que el patron de orden es el mismo en las dos cadenas


lista1=("a" "a" "a" "b" "b" "c" "d" "e")
lista2=("pato" "pato" "pato" "mano" "mano" "perro" "gato" "jirafa")

len_lista1=${#lista1[@]}
len_lista2=${#lista2[@]}

if [[ $len_lista1 != $len_lista2 ]]; then
    echo "lengt is not equal"
    exit 1
fi

declare -A newmap
declare -A newmap2

for i in {1..$len_lista1}
do
    key=${lista1[$i]}
    if [[ ${newmap[$key]} != "" ]]; then
        key2=${lista2[$i]}
        if [[ ${newmap2[$key2]} != "" ]]; then
            echo "listas no coinciden 0"
            exit 1
        fi
        if [[ ${lista2[$i]} != ${newmap[$key]} ]]; then
            echo "listas no coinciden 1"
            exit 1
        fi

    else 
        newmap[$key]=${lista2[$i]}
        newmap2[${lista2[$i]}]=$key
    fi
done
echo "end of file"