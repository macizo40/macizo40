#!/bin/bash
#Hacer un programa que determine el area de un triangulo

base=5
altura=7

function area_triangulo(){
    base=$1
    altura=$2
    resultado=$(($base*$altura/2))
    echo $resultado
}


area1=$(area_triangulo "$base" "$altura")
area2=$(area_triangulo "8" "5")
echo $area1
echo $area2