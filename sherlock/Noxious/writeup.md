# Noxious 


## General Notes 


- LLMNR - Link-Local Multicast Name Resolution 
  - Port 5355
- NTLM -> Network LAN Manager
  - Is a Challenge and Response authentication protocol used to authenticate a client to a resource on an Active Directory Domain. 
  - If you get the ntlm challenge and the ntlm proof you should be able to try to crack it in Hashcat. 
- Hashcat -a0 -m5600 hashfile.txt rockyouwordlist.txt 




 
  





Learnings:
  - When checking for dhcp and a specific IP you can figure out when the IP was assigned to a specific host -> Getting hostname etc. 
  - NTLMSSP -> NT LAN Manager Security Support Provider -> Binary message protocol to facilitate NTLM challenge-response authentication. 

In wireshark you can filter for:
  - Port 5355 and UDP  (udp.port == 5355)
  - Using Statistics -> Endpoints to get requency 



9291	.921154	fe80::2068:fe84:5fc8:efb7	fe80::7994:1860:711:c243	SMB2	412	Session Setup Response, Error: STATUS_MORE_PROCESSING_REQUIRED, NTLMSSP_CHALLENGE