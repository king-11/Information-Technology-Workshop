#!/bin/bash

echo -n "Enter a string : "
read str

r=$(echo "$str" | rev)
if [ "$r" = "$str" ];
then 
	printf "It's a Palindrome"
else
	printf "Not a Palindrome"
fi
