# Enumeration

## Port 80 - HTTP
### Dirsearch

using `dirsearch -u http://10.10.10.242 `

```
Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/chris/Documents/Github/HTB-Writeups/reports/_10.10.10.242/_24-11-26_10-49-25.txt

Target: http://10.10.10.242/

[10:49:25] Starting: 
[10:49:27] 403 -  277B  - /.ht_wsr.txt
[10:49:27] 403 -  277B  - /.htaccess.bak1
[10:49:27] 403 -  277B  - /.htaccess.orig
[10:49:27] 403 -  277B  - /.htaccess.sample
[10:49:27] 403 -  277B  - /.htaccess.save
[10:49:27] 403 -  277B  - /.htaccess_extra
[10:49:27] 403 -  277B  - /.htaccess_orig
[10:49:27] 403 -  277B  - /.htaccessBAK
[10:49:27] 403 -  277B  - /.htaccess_sc
[10:49:27] 403 -  277B  - /.htaccessOLD
[10:49:27] 403 -  277B  - /.htaccessOLD2
[10:49:27] 403 -  277B  - /.html
[10:49:27] 403 -  277B  - /.htm
[10:49:27] 403 -  277B  - /.httr-oauth
[10:49:27] 403 -  277B  - /.htpasswds
[10:49:27] 403 -  277B  - /.htpasswd_test
[10:49:45] 403 -  277B  - /server-status/
[10:49:45] 403 -  277B  - /server-status

Task Completed
```
### Gobuster


