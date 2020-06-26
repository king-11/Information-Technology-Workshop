# @Author: Lakshya Singh Jatin Garg
# @Date:   2020-02-18T01:05:23+05:30
# @Email:  lakshay.singh1108@gmail.com jatin.garg.cse19@itbhu.ac.in
# @Last modified by:   target-x rivalq
# @Last modified time: 2020-02-18T13:29:06+05:30


isexpert=1
if [  "$#" -eq  "0"  ]
  then
  isexpert=0
  echo "         UNIX HELP MAIN MENU         "
  echo "                                     "
  echo "1 -- File and Directory Management Commands"
  echo "2 -- Text Processing Commands"
  echo "3 -- System Status Commands"
  echo "4 -- Exit"
  echo "                                     "
  echo -n "Enter your choice: "
  read choice
  while [ $choice -ne 1 -a $choice -ne 2 -a $choice -ne 3 -a $choice -ne 4 ]
   do
     echo -n "Enter a valid choice: "
     read choice
   done
  if [ $choice -eq 1 ]
   then
    echo -n "Opening the File management Submenu "
    ./spinner.sh sleep 3
    #echo ""
    clear
    exec ./file.sh $isexpert
  elif [ $choice -eq 2 ]
   then
     echo -n "Opening the Text Processing Submenu "
    ./spinner.sh sleep 3
    #echo ""
    clear
    exec ./text.sh $isexpert
  elif [ $choice -eq 3 ]
   then
     echo -n "Opening the System Status Submenu "
    ./spinner.sh sleep 3
    #echo ""
    clear
    exec ./system.sh $isexpert
  else
    echo "Exiting the program"
    ./spinner.sh sleep 3
     exit 
   fi
elif [ "$1" != "help" -a "$1" != "status" -a "$1" != "text" -a "$1" != "file" ]
   then
    echo "Enter a valid argument"
    echo "Exiting the Program"
    exit 1
elif [ "$1" == "file" ]
   then
    echo -n "Opening the File management Submenu "
    ./spinner.sh sleep 3
    #echo ""
    clear
    exec ./file.sh $isexpert
elif [ "$1" == "text" ]
   then
    echo -n "Opening the Text Processing Submenu "
    ./spinner.sh sleep 3
    #echo ""
    clear
    exec ./text.sh $isexpert
elif [ "$1" == "status" ]
   then
    echo -n "Opening the System Status Submenu "
    ./spinner.sh sleep 3
    #echo ""
    clear
    exec ./system.sh $isexpert
elif [ "$1" == "help" ]
   then
    echo -n "About the program"
    ./spinner.sh sleep 3
    #echo ""
    clear
    exec ./help.sh
fi
