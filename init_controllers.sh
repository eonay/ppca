#!/bin/bash
c0='192.168.88.111'
c1='192.168.88.222'




fping -c1 -t300 $c0 2>/dev/null 1>/dev/null
if [ "$?" = 0 ]
then
  echo "c0 funcionando"
else
  echo "problema c0"
fi



fping -c1 -t300 $c1 2>/dev/null 1>/dev/null
if [ "$?" = 0 ]
then
  echo "c1 funcionando"
else
  echo "problema c1"
fi