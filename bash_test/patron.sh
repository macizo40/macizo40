#!/bin/bash

# Función para generar el patrón de una cadena
generar_patron() {
    local cadena=$1
    local patron=""
    local contador=97
    declare -A mapa

    # Recorrer las palabras de la cadena
    for palabra in $cadena; do
        if [ -z "${mapa[$palabra]}" ]; then
            mapa[$palabra]=$(printf \\$(printf '%03o' $contador))
            contador=$((contador + 1))
        fi
        patron="$patron${mapa[$palabra]}"
    done

    echo "$patron"
}

cadena1="a a b b c c"
cadena2="perro perro gato gato mano mano"

patron1=$(generar_patron "$cadena1")
patron2=$(generar_patron "$cadena2")

if [ "$patron1" == "$patron2" ]; then
    echo "Las cadenas tienen el mismo patrón en su contenido."
else
    echo "Las cadenas NO tienen el mismo patrón en su contenido."
fi