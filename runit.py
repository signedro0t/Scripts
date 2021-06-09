#!/usr/bin/env python3
import subprocess

#Run Standard ro0t nmap scan
print('\n')
print('[+]ShockWave in progress.....','\n', '[+]Opening Nmap.....', '\n')
subprocess.run('nmap -oN scan.txt 127.0.0.1', shell=True, check=True)


#Run Nikto
print('\n')
print('[+]Nikto in progress.....')
#subprocess.run('nikto -C all -host (127.0.0.1)', shell=True, check=True)
subprocess.run('nikto')

#Run Gobuster if applicable
print('\n')
print('[+]Gobuster in progress.....')
subprocess.run('gobuster 127.0.0.1')
print('\n')
print('Initial scans complete!')

