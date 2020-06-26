#!/bin/bash

echo -n "Enter name of file :"
read name
echo " "
if [ -f $name ];
then 
	cat $name
elif [ -d $name ];
then
	ls $name
fi
echo " "
ls -l | grep "^-rw"
