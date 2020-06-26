#!/bin/bash

echo -n 'How many prime numbers to print: '
read n
cnt=0
i=2
echo 'Here are the first' $n 'primes'
while [ $cnt -ne $n ];
do
  f=0
  for ((j=2 ;j<i;j++))
  do 
     if [ $j -ne 1 ];
      then
       r=$((i%j))
       if [ $r -eq 0 ];
        then
         f=1
        fi
      fi
  done
  if [ $f -ne 1 ];
   then
    cnt=$((cnt+1))
    echo -n $i
    echo -n " "
   fi 
   i=$((i+1))
done
echo "" 