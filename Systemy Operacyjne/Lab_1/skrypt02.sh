#1/bin/bash

if [ $# -ne 2 ]
then echo "Wrong number of arguments, two required!"; exit 1
fi

min=$1
max=$2
range=$(($max-$min+1))
random=$(($min+$RANDOM%$range))

echo "Random number generated, try your luck!"
read guess

while [ $guess -ne $random ]
do

	if [ $guess -le $random ]
	then
		echo "Random number is bigger!"			
	else
		echo "Random number is lower!"
	fi

	echo "Try again!"
	read guess
	
done
