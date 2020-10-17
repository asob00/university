#!/bin/bash
pdf_file=$1
png_file=$2
x=$3
y=$4
convert -density 144 -size $(identify -format "%wx%h" "$pdf_file") xc:transparent \( "$png_file" -resize 100% \) -geometry +$x+$y -composite "$pdf_file"
