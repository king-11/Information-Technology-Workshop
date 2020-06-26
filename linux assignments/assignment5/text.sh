#!/bin/bash
if [ $1 -eq 1 ];
then
printf "\t\t\tTEXT PROCESSING COMMANDS\n\n 1 -- Search a file for a pattern
\n 2 -- Count lines, words, and characters in specified files
\n 3 -- Display line differences between two files
\n 4 -- Exit Program
\n\n\t\t\t Enter your choice:\n\n" | more
else
printf "\t\t\tTEXT PROCESSING COMMANDS\n\n 1 -- Search a file for a pattern
\n 2 -- Count lines, words, and characters in specified files
\n 3 -- Display line differences between two files
\n 4 -- Quit -- Return to Main Menu
\n\n\t\t\t Enter your choice:\n\n" | more
fi

read opt

while ((1));
do
if [ "$opt" -eq 1 ];
then
    printf "\nEnter file to check for pattern : "
    read filename
    echo ""
    echo -n "Enter pattern to search for :"
    read pattern
    echo ""
    grep -E $pattern $filename
    echo ""
elif [ "$opt" -eq 2 ];
then
    printf "\nEnter filename : "
    read filename
    echo ""
    echo -n "Number of line : "
    wc -l $filename | awk '{ print $1 }'
    echo ""
    echo -n "Number of words : "
    wc -w $filename | awk '{ print $1 }'
    echo ""
    echo -n "Number of characters : "
    wc -c $filename | awk '{ print $1 }'
    echo ""
elif [ "$opt" -eq 3 ];
then
    printf "\nEnter files to chech pattern in : "
    read filename
    echo ""
    diff ${filename[0]} ${filename[1]}
    echo ""
elif [ "$opt" -eq 4 -a $1 -eq 0 ];
then
  ./spinner.sh sleep 3
  #echo ""
  clear
    exec ./myhelp.sh
elif [ "$opt" -eq 4 -a $1 -eq 1 ];
then
  echo "Exiting Program"
  ./spinner.sh sleep 3
  exit
else
    echo "Select a valid option please !"
fi
echo -n "Select from above options : "
read opt
done
