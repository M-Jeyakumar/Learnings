#!/bin/bash
# Program to counts from zero to one
echo $*
echo $1

if [[ $1 == arg1 ]]
then
  echo true
else
echo false
fi


if [[ $1 -le 5 ]]
then
  echo true
else
echo false
fi


if [[ $1 -gt 0 ]]
then
  echo true
else
  echo Include a positive integer as the first argument.
fi



#!/bin/bash
# Program to counts from zero to one
echo -e "\n~~ Countdown Timer ~~\n"
if [[ $1 -gt 0 ]]
then
  : 'for (( i = $1; i>=0; i-- ))
  do
    echo $i
    sleep 1
  done
  '
  I=$1
  while [[ $I -ge 0 ]]
  do
    echo $I
    (( I-- ))
    sleep 1
  done
else
  echo Include a positive integer as the first argument.
fi





: ' 
0-true
1-false

You can compare integers inside the brackets ([[ ... ]]) of your if with -eq (equal), 
-ne (not equal), -lt (less than), -le (less than or equal), -gt (greater than), -ge (greater than or equal). 
'
