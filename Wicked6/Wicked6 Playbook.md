# Wicked6 Playbook

## AU Cyber Defense Team

This is a preliminary draft. We should want to prioritize tools and techniques for security domains
relevant to the competition. Tools should have links to the domains, and techniques should be cited if possible. This playbook should focus on being short and concise. It should be a reference guide and not a tutorial.

### Domains

* Architecture

* Network Security
  * Firewalls -> (VFW, Windows Defender, Cisco)
    * iptables

* Data Protection  

* Identity Management

* Cryptography  

### Risk Assesment

* Vulnerability Scan

* Penetration Testing

* Data Flow Mapping

* Binary Analysis  

### Threat Intelligence

* Internal Sources

* Technical Sources

* Human Sources  

### Security Operations

* Protection

* Detection
  * ping, traceroute/tracrt, hping, arpscan, nmap, plunk
  * Wireshark, firewall, Tcpdump, Network Monitor

* Recovery

* Vulnerability
  * nmap -vuln, openVas, exploitDB, searchsplit, lynis(?)

* Data Leakage  

### Incident Response

* Notification

* Containment

* Eradication
  
* Forensics  
  * Find, File, (Stuff from bandit)
  * binwalk

## Circadence

### System Integrator

* `ping <ip>`
* `ping -s 9999`
* `sudo hping3 -1 --icmptype 13 <ip>`
* `traceroute <ip>`
* `nmap -sS <ip>`
* `nmap -sF <ip>`
* `nmap -sX <ip>`
* `nmap -sV <ip>`
* `nmsap -O <ip>`
* `nmap -sS -p- <ip>` 
* `nmap --script=vuln <ip>`
* `nmap --script=smb-enum-shares <ip>`
* `dig <hostname>`
* `nslookup <hostname <DNS server ip>>`

### Network Analyst

* `netstat -an`
* `cat cisco-cfg.txt | grap password | grep -v "service \|username" | wc -l`
* `>>>cisco_CLI>>> permit host <ip>`  

### Intel Analyst

All of these except the last are 100% done in the Maltego interface. The last you just look at the jpeg and find what they ask for.
1.  Open the file in Maltego -> Find the desired domain (comcast) -> secure.circadence.com
2.  Open the file in Maltego ->  Find the blog post specified by mousing over nodes on the tree -> grab the source domain -> powermag.com
3.  Open the file in Maltego -> look through the tree's children to find the source company -> Microsoft
4.  Open the file in Maltego -> Look through the emails in the tree to find sub-domains -> toronto.circadence.com
5.  Find the tweet through the tree -> grab the handle from the right sidebar -> epic_joel
6.  Find the hashtag from the right sidebar -> #opsec
7.  Open the Jpeg -> use eyes to parse launguages mentions -> Find the one with 4 mentions -> Portuguese

### Forensics One

* item a
* item b
* item c
