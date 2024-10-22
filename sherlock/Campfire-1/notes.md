# Campfire 1 

Challenge: https://app.hackthebox.com/sherlocks/Campfire-1/play 


## Given 

1. Security Logs from Domain Controller
2. PowerShell-Operational Logs from the affected workstation 
3. Prefetch Files from the affected workstation 


## General Notes 


Prefetch:
   - Prefetch Files -> Usualy *.pf files inside the path: `C:\Windows\Prefetch`
   -  Tool required PEcmd.exe 

Kerberoasting:
  - Optain a password hash of AD that has a SPN name 

1. User requests an Kerberos ticket for an SPN
2. Ticket encrypted with hash of SA password affilita with SPN. 
3. Adversary works offline to crack the password hash, often using Brute force techinques 



TGS -> Kerberos Ticket granting Service 
KDC -> Kerberos Distribution Center  -> Sends encrypted ticket + hashed version of the password 


Three Heads of Kerberos
  - Principle -> Identity that wishes to authenticate -> User Principal or Service Principal
  - Resource - Asset or Service client aims to reach
  - KDC - Key Distribution Center 

Typical tool used for this -> GetUserSPNs tool


## What should I be able to detect in the log files 


- Powershell Operational Logs -> 

IP Attack is coming from -> 172.17.79.129 