#!/bin/bash

echo -n "Enter a string: "
read x

y=$(echo "$x" | rev)

if [ "$x" = "$y" ]; then
	echo "It is palindrome"
else
	echo "Not a palindrome"
fi
