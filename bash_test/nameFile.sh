#!/bin/bash

#Pregunta: Escribe un script en Bash que acepte un nombre como argumento y 
#luego verifique si ese nombre es un archivo o un directorio en el directorio actual. 
#Si es un archivo, imprime "Es un archivo". Si es un directorio, imprime "Es un directorio". 
#Si no existe, imprime "El archivo o directorio no existe".

content1=folder
content2=area
content3=salomon

function file_or_folder(){
    artifact=$1
    folder=$(find . -type d -name "$artifact*")
    file=$(find . -type f -name "$artifact*")

    if [[ $folder != "" ]]; then
        echo "es un folder"
        
    elif [[ $file != "" ]]; then
        echo "es un file"
    
    else
        echo "El archivo o directorio no existe"
    fi
}

area1=$(file_or_folder "$content3")
echo $area1
