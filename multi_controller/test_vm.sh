#!/bin/bash
#

QTD="2" 

clear
ping -c $QTD 192.168.219.128 
clear
echo "Run Mininet ..."
echo "...[OK]" 

sleep 3

clear 
ping -c $QTD 192.168.219.111 
clear
echo "Run Controller Ryu [1]..."
echo "...[OK]"

sleep 3

clear 
ping -c $QTD 192.168.219.222
clear
echo "Run Controller Ryu [2]..."
echo "...[OK]"


sleep 3

clear
echo "Ryu [1] ... ...[OK]"
echo "Ryu [2] ... ...[OK]"
echo "Mininet ... ...[OK]"
