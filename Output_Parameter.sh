#!/bin/bash
if test -f `pwd`/output.txt;then
        rm -rf `pwd`/output.txt
fi
curl 10.142.0.2:80/palindrome/$1 >> output.txt
echo " " >> output.txt
echo " "
cat output.txt
