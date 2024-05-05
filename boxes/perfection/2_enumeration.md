# Enumeration


## Port 80 - HTTP

### DirBusting
#### Dirsearch

Using `dirsearch -u http://10.10.11.253/` provides the following output:

```
Target: http://10.10.11.253/

[21:55:03] Starting:
[21:55:10] 200 -    4KB - /about

Task Completed
```

#### Using dirbuster

Using dirbuster `dirbuster -l /usr/share/dirbuster/wordlists/directory-list-1.0.txt -t 30 -R -u http://10.10.11.253 `

Only resulted in the following paths

- `/about`
- `weighted-grade`



### Vulnerability Scanning


#### Nessus

- No useful information found

#### Whatweb

Using the following command `whatweb -a=4 --colour --log-json=whatweb_log.json http://10.10.11.253`

-> Whatweb was actually never properly working... so no information
