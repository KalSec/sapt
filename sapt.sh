#!/bin/bash 
clear
# ascii art of sapt

echo "                    ___    __    ____  ____                    "
echo "                   / __)  /__\  (  _ \(_  _)                   "
echo "                   \__ \ /(__)\  )___/  )(                     "
echo "                   (___/(__)(__)(__)   (__)                    "
echo "                                                               "
echo "          """Semi Automated Penetration Testing""" by kal      "
echo "                                                               "

# checking for root/sudo

echo "[+] Checking for root"

if [[ $EUID -ne 0 ]]; then
        echo "[-] SAPT must be run as root"; exit 1
fi

# checking for requirements
 
echo "[+] checking for requirements"

requirements=(nmap nc foo bar)
for i in "${requirements[@]}"; do
        command -v $i >/dev/null || { echo "I require $i but it's not installed."; }
done
