#!/bin/bash
#

QTD="5" 

clear
ping -c $QTD 192.168.88.88 
clear
echo "Run Mininet ..."
echo "...[OK]" 

sleep 3

clear 
ping -c $QTD 192.168.88.111 
clear
echo "Run Controller Ryu [1]..."
echo "...[OK]"

sleep 3

clear 
ping -c $QTD 192.168.88.222
clear
echo "Run Controller Ryu [2]..."
echo "...[OK]"


sleep 3

clear
echo "Ryu [1] ... ...[OK]"
echo "Ryu [2] ... ...[OK]"
echo "Mininet ... ...[OK]"