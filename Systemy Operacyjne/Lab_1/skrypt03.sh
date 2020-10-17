#!/bin/bash
podstawa=$1
potega=$2
wynik=1
for ((n=0;n<$potega;n++))
do
	wynik=$(($wynik*$podstawa))	
done
echo $wynik
 
