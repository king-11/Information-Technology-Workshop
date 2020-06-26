echo "        FILE AND DIRECTORY MANAGEMENT COMMANDS      "
echo "                                                    "
echo 1 -- Display the contents of a file
echo 2 -- Remove a file
echo 3 -- Copy a file
echo 4 -- List a file
echo 5 -- Size of a file
if [ "$1" == "1" ]
 then 
  echo 6 -- Exit the program
else  
 echo 6 -- Quit -- Return to main Menu
 fi
echo ""
echo -n "Enter your choice: " 
read choice
while [ 1 ]
do
while [ $choice -ne 1 -a $choice -ne 2 -a $choice -ne 3 -a $choice -ne 4 -a $choice -ne 5 -a $choice -ne 6 ]
   do 
     echo -n "Enter a valid choice: "
     read choice
   done
if [ $choice -eq 1 ]
 then
  echo -n 'Enter the Path of File which you want to view: '   
  read file
  while [ ! -f $file  ]
   do 
    echo -n "Enter Valid Path: "
    read file
   done  
  cat $file
 fi 
if [ $choice -eq  2 ]
 then 
  echo -n 'Enter the Path of File which you want to remove: '   
  read file
  while [ ! -f $file1  ]
   do 
    echo -n "Enter Valid Path: "
    read file
   done  
  rm $file
  echo $file removed
 fi
if [ $choice -eq 3 ]
 then 
  echo -n 'Enter the Path of File which you want to copy: '   
  read file1
  while [ ! -f "$file1"  ]
   do 
    echo -n "Enter Valid Path: "
    read file1
   done  
  echo -n 'Enter the Destination Path: ' 
  read file2
  while [ ! -d "$file2"  ]
   do 
    echo -n "Enter Valid Path: "
    read file2
   done  
  cp $file1 $file2
  echo $file1 copied to $file2
fi 
if [ $choice -eq  4 ]
 then 
  echo -n 'Enter the Path of File which you want to list: '   
  read file
  while [ ! -f $file1  ]
   do 
    echo -n "Enter Valid Path: "
    read file
   done  
  ls  -l $file
 fi
if [ $choice -eq  5 ]
 then 
  echo -n 'Enter the Path of File: '   
  read file
  while [ ! -f $file1  ]
   do 
    echo -n "Enter Valid Path: "
    read file
   done  
  ls -sh $file | awk '{ if(NR==1) print $1 }'
 fi 
if [ $choice -eq 6 ]
 then 
  if [ "$1" == 1 ]
   then 
    echo Exiting the program
    exit 1
  else
   clear
   echo "Opening main menu"
   ./myhelp.sh
   fi
fi
echo -n 'Enter Your Choice: '
   read choice      
done
    
    