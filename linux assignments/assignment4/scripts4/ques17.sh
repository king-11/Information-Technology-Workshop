#!/bin/bash
read a
b=0
while [ $a -ne 0 ]
do
  b=$((b*10))
  b=$((b+a%10))
  a=$((a/10))
 
done
echo $b
