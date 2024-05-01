#!/bin/bash

nombre=$1

if [ -f "$nombre"* ]; then
    echo "Es un archivo"
elif [ -d "$nombre"* ]; then
    echo "Es un directorio"
else
    echo "El archivo o directorio no existe"
fi