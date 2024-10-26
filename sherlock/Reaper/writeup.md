# Reaper Write-Up


## First ideas 

Search in Wireshark for some useful information 



## General Notes 

About Protocols:
  - NBNS - NetBIOS Name Service -> Similar to DNS translates human-readable names to ip addresss
  - IGMP - Internet Group Management Protocol (used for multicasting)
  - ICMP - Internet Control Message Protocol
  - ARP - Address Resolution Protocol -> Used to discover linked layer addresses such as MAC
  - MDNS - Multicast DNS -> Used for resolving host names to IP addresses within small networks that do not include DNS server. 
  - SSDP - Simple Service Discovery Protocol -> used for networked devices to communicate and discover each other 
  - DHCP Flow 
    1. MAC of Device  ->  "DHCP Disccover" -> Broadcast to identify the DHCP Server
    2. DHCP Server IP -> "DHCP Offer" -> Mac of Device ("DHCP Server on the network receives the Ethernet broadcast and offers an IP")
    3. PC accets the IP address offered by the DHCP server 
    4. Mac of Device -> "DHCP Request" -> "Braodcast"
    5. Maco of Device <- "DHCP Ack"
- 
