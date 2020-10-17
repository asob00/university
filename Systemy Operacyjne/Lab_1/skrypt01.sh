#!/bin/bash

KATALOG="$1"
WIELKOSC="$2"

set -f
IFS='
'
valid_path='^/'
valid_file='^-'
best_file=""
current_path=""
for file in $(ls -laR --full-time "$KATALOG" | sort -k 6,7 -n)
do
	if [[ $file =~ $valid_file ]]
	then
		size=$(echo $file | tr -s ' ' | cut -d " " -f 5)
		if [[ $size -ge $WIELKOSC ]]
		then
			echo "$file"
			exit 0
		fi
	fi
done
