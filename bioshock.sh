#!/bin/bash

echo "[+] Welcome To BioShock"
echo "[+] Commencing Enumeration. May the Odds Be Ever in Your Favor -_-"
echo "[-] First things first, tell me your name: "
read name
fn=$(whoami)

if $name == $fn
then
    echo "YOU ARE THE EPITOME OF ROOT O_0"
else
    echo "Step Away...You Will"
fi 

echo "[+] Nmap'N"

scan=$(nmap -p22 127.0.0.1)
echo $scan
echo 
echo "[+] Ahhh shiiii, Now We're Moving...."
ost=$(history | grep nmap)
echo $ost
echo

hom=$(whoami)
echo $hom


