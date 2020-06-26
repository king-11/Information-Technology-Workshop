#!/bin/bash

for i in $(seq 999)
do 
	a=$((i % 10))
	b=$((i/10))
	b=$((b%10))
	c=$((i/100))
	sum=$(((a*a*a) + (b*b*b) + (c*c*c)))
	if [ $sum -eq $i ];
	then
		echo $sum
	fi
done
