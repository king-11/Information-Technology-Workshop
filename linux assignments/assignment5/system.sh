#!/bin/bash

if [ $1 -eq 1 ];
then
printf "\t\t\tSYSTEM STATUS COMMANDS\n\n 1 -- Display the current date and time
\n 2 -- Current disk usage
\n 3 -- List current local and enviornmental
\n 4 -- Display process status information
\n\n 5 -- Exit Program;
\n\n\t\t\t Enter your choice:\n\n" | more
else
printf "\t\t\tSYSTEM STATUS COMMANDS\n\n 1 -- Display the current date and time
\n 2 -- Current disk usage
\n 3 -- List current local and enviornmental
\n 4 -- Display process status information
\n\n 5 -- Quit -- Return to Main Menu
\n\n\t\t\t Enter your choice:\n\n" | more
fi

read a
printf "\n"

while ((1))
do
if [ "$a" -eq 1 ];
then
    echo ""
    date +"%d/%h/%Y %R"
    echo ""
elif [ "$a" -eq 2 ];
then
    echo ""
    df | more
    echo ""
elif [ "$a" -eq 3 ];
then
     echo ""
     printenv | more
     echo ""
elif [ "$a" -eq 4 ];
then
    echo ""
    ps -e | more
    echo ""
elif [ "$a" -eq 5 -a "$1" -eq 0 ];
then
  ./spinner.sh sleep 3
  #echo ""
  clear
    exec ./myhelp.sh
elif [ "$a" -eq 5 -a "$1" -eq 1 ];
then
    echo "Exiting Program"
    ./spinner.sh sleep 3
    exit
else    
    echo "Select a valid option !"
fi
echo -n "Select from above options : "
read a
done
