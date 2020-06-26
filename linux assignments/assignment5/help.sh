#!/bin/bash

printf "\t\t----- Welcome to Mini Project by Lakshya and Jatin -----\n
\t $ To perform any task on this system all you have to do in select your choice of options from given. $\n
# In File Menu you will find commands like ls, cat, cp etc.\n
# In System Status Menu you will find commands like ps, df, date, printenv\n
# In Text Menu you will find commands like grep, diff, wc\n\n"

echo "@Author: Lakshya Singh Jatin Garg"
echo "@Date:   2020-02-18T01:05:23+05:30"
echo "@Email:  lakshay.singh1108@gmail.com jatin.garg.cse19@itbhu.ac.in"
echo "@Last modified by:   target-x rivalq"
echo "@Last modified time: 2020-02-18T13:29:06+05:30"

printf "\n\n ------ \tPress any key to go back to main program ------\n"
read opt
./spinner.sh sleep 3
clear
exec ./myhelp.sh
