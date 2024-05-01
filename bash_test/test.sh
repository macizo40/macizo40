#!/bin/bash
#Hacer un programa que recorra un arreglo de cadenas e imprima en pantalla las cadenas que contengan la letra a

cadenas=("cadenas" "mundo" "programar")

for cadena in "${cadenas[@]}"
do
    if [[ $cadena == *"a"* ]]; then
        echo "$cadena Contains a"
    fi
done
