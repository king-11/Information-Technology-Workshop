#!/bin/bash

read -p "Enter length :" l
read -p "Enter breadth :" b

function area(){
	x=$1
	y=$2
	echo "$((x*y))"
}
 
area l b
