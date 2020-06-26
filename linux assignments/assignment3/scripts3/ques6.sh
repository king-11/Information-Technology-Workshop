#!/bin/bash

echo -n "Enter Larger number "
read larg
printf "\nEnter Smaller number "
read sml

while [ "$larg" -le 0 ];
do
	echo -n "Enter correct input for large "
	read larg
done

while [ "$sml" -le 0 ];
do
	echo -n "Enter correct input for small "
	read sml
done

echo "scale=5; $larg/$sml" | bc



