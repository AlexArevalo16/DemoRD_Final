#!/bin/bash
clear; clear;
if test -f `pwd`/output.txt; then
        rm -rf `pwd`/output.txt
fi
day=$(date +%A)
month=$(date +%B)
day_month=$(date +%d)
year=$(date +%Y)
hour=$(date +%r |sed 's/:/ /g' |awk '{print$1":"$2,$4}')

echo " "
echo -e "\t\t\e[44m $day $day_month $month $year $hour \e[0m"
echo " "
echo -e "\t\e[36m   ----- Check Output from Palindrome, RD_DEMO -----\e[0m"
echo " "

function owner(){
        echo " "
        echo -e "\e[36m Powered by @Alejandro Arevalo\e[0m"
        echo " "
}

function output(){
        read -p "How many times do you want to hit the API: " tms
        read -p "Please enter a word: " word
        i=1
        while [ $i -le $tms ]
                do
                        curl localhost:80/palindrome/$word >> output.txt
                        echo " " >> output.txt
                        echo "---------- Output No $i ----------" >> output.txt
                        sleep 1
                        let i+=1
                done
                owner 
}
output
