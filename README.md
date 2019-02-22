
# CCDC PLAYBOOK 2019

Official playbook for AU-ACM Cyber Defense Club 


# Table of Contents

## Primary Goals
CCDC is a yearly blue vs red competition.

The objective: maintain up time of an enterprise network and its primary services all while protecting the network from a professional red team.  

The enterprise network architecture changes each year,
meaning each year team composition should change to meet the challenges presented by the newest iteration of the play field.

/add image here/

## Scoring

## Team Composition
Our team composition this year is a close mapping of the enterprise architecture, with Captain and Change Control Officer designated to carry out tasking injections to any of three teams: Windows, Unix, and Firewall administration.
 
 ```mermaid
graph LR
A(Change Control Officer) --> B(Captain)
C(Windows Team) --> A
D(Linux Team) --> A
E(A/D DNS) --> C
F(Exchange) --> C
G(BIND DNS) --> D
H(E-Commerce) --> D
I(Web Apps) --> D
J(Network Admin) --> A
```

This is a team competition, where coordination and communication are imperative to success.

## The Game Plan
**Injects** and **Incidents** are prioritized.
- Injects correspond to tasks received by the Captain. The entire team is responsible for completing each inject.
- Incidents correspond to primary services taken down by the red team or *otherwise* 

To successfully balance inject completion, incident resolution all while maintaining or improving a security posture, refer to this work flow:
 
 ```mermaid
graph LR
A(Inject Completion) --> B(Initial Hardening)
B --> C(Harden)
C --> D(Enumerate)
D --> E(Hunt)
A --> C
E --> A
A --> F(Incident Resoultion)
F --> C
```

## Injects
Injects are most often tasks associated with system administration tasks.
/example inject/

Each team is responsible for: 
- Resolving injects tasked to that team 
- Proper documentation 
- Communicating with other teams 

## Incidents
The entire team is responsible for maintaining fundamental services:
- #### HTTP
- #### HTTPS
- #### Webmail-HTTP
- #### SMTP
- #### POP3
- #### DNS

Each team is responsible maintaining the services under their purview:
- #### Firewall
	- Egress and Ingress Rules for all fundamental services
- #### Windows
	- AD DNS 
	- Webmail-HTTP
	- POP3
- #### Linux
	- HTTP/HTTPS
	- DNS
	- SMTP

## Hardening
There should be no injects given within the first 15 minutes. Hardening each and every device under your purview is the first step that should be taken towards securing a system. Since hardening a system is never completely finished, break hardening up into an initial step and a recurrent process. 

The initial step breaks down neatly into three smaller, consecutive steps:

&nbsp;&nbsp;1. new user passwords
&nbsp;&nbsp;2. configure admin accounts
&nbsp;&nbsp;3. access rights 

### These steps differ slightly per team.

#### - Network Admin 
&nbsp;&nbsp;1. Change Default Credentials

&nbsp;&nbsp;2. Harden Admin Account

&nbsp;&nbsp;3. Define Firewall Rules   

#### - Windows Team
&nbsp;&nbsp;1. Change Default Credentials

&nbsp;&nbsp;2. Create an Admin Account

&nbsp;&nbsp;3. Restrict Login Access

log successful and failed logins
```powershell
auditpol.exe /set /category:"Logon/Logoff"  /success:enable /failure:enable | out-null
```

#### - Linux Team

&nbsp;1. change default user credentials
```bash
# change default password for default login
passwd
# open a root shell and change root password
sudo -i 
passwd
usermod -l <newname> <oldname>
usermod -d ~/home/<newname> -m <newname>
# symlink $HOME 
ln -s ~/home/<newname> ~/home/<oldname> 
```
&nbsp;2. configure wheel and add an admin

*add the **wheel** group if it doesn't already exist!* 
```bash
groupadd wheel
```
*Restrict the use of sudo to the wheel group by configuring **/etc/sudoers**.*
*Use **visudo** and uncomment the following:*
```bash
wheel ALL=(ALL) ALL  
```
*Restrict use of su with pam.*
*Uncomment or add the following line to **/etc/pam.d/su**:*
```bash
auth		requirement	pam_wheel.so group=wheel
```
*while root create an admin account:*
```bash
useradd -mg wheel <admin>
passwd <admin> 
exit
# login as admin and restrict root login and su to <admin>
sudo -i -u <admin>
sudo passwd -l root 
sudo chown <admin>:wheel /bin/su
```
#####  &nbsp;&nbsp;&nbsp;&nbsp;**Use sudo -i -u adminname when performing admin tasks!*

&nbsp; 3. Restrict Login Access  

```bash
/etc/pam.d/system-login

# Set a delay upon authentication failure
# Lock out a user after 3 repeated failed attempts
auth optional pam_faildelay.so delay=4000000
auth required pam_tally2.so deny=3 unlock_time=600 onerr=succeed file=/var/log/tallylog
```

```bash
/etc/security/limits.conf

#Limit processes run by users
* soft nproc 100
* hard nproc 200
```
## Enumeration
### Firewall
### Windows
### Linux 

**nmap**

**ss**

**ps**

**pstree**

#### Maintaining Services
##### systemctl
```bash
# to get service status:
systemctl status <service>  # you can omit <service> to list all as a tree
# to list running services or failed services:
systemctl | grep running
systemctl --failed
# to start, stop, restart a status: 
systemctl start <status>
systemctl restart <status>
systemctl stop <status>
# to enable or disable a service:
systemctl enable <service>
systemctl disable <service>
```
##### journalctl
```bash
# show all messages since 20 minutes ago:    
journalctl --since "20 min ago"
# follow new messages:
journalctl -f
# show all messages by a specific executable:
journalctl /usr/lib/systemd/systemd
# show all messages by a specific process:
journalctl _PID=1
# show all messages by a specific unit:
journalctl -u <service>
# show kernel ring buffer:
journalctl -k
```

## Hunting

### Windows Team


### Linux Team

#### File Permissions

|  |Owner|Group|Other|
|--|-----|-----|-----|
|r |  4  |  4  |  4  |
|w |  2  |  2  |  2  |
|x |  1  |  1  |  1  |

**find**
```bash
# Note: /path/to/file refers to any path (. ./ /home /etc ..)
# print files owned by a user
find /path/to/file -user <user>
# print .ext files owned by a user
find /path/to/file -user <user> -name "*.ext"
# you can do the same but by group 
find /path/to/file -group <group> -name "*.ext"
# print all shell files owned by usera and userb with ls formatting
find /path/to/file -name "*.sh" -user usera userb -ls
# you can also use logical operators
# -o -or, ! -not, -a -and (^^implicit without operators)
find /path/to/file -name "*.sh" -user usera -o userb -ls
# delete all files owned by a user
find /path/to/file -user <badguy> -delete
```

**chown**
```bash
# change ownership of a file to <user>:<group>
chown <user>:<group> /path/to/file
# change ownership to admin of a folder and all subfolders
chown -hR admin /directory

```
**chmod**
|  |Owner|Group|Other|
|--|-----|-----|-----|
|r |  4  |  4  |  4  |
|w |  2  |  2  |  2  |
|x |  1  |  1  |  1  |
```bash
# change access mode of a folder or file
chmod <o,g,e>
# 
chmod 0700 
chmod 0077 /boot /etc/{iptables,artptables}
```
**kill**
```bash
#
```

#### Maintaining Services
##### systemctl
```bash
# to get service status:
systemctl status <service>  # you can omit <service> to list all as a tree
# to list running services or failed services:
systemctl | grep running
systemctl --failed
# to start, stop, restart a status: 
systemctl start <status>
systemctl restart <status>
systemctl stop <status>
# to enable or disable a service:
systemctl enable <service>
systemctl disable <service>
```
##### journalctl
```bash
# show all messages since 20 minutes ago:    
journalctl --since "20 min ago"
# follow new messages:
journalctl -f
# show all messages by a specific executable:
journalctl /usr/lib/systemd/systemd
# show all messages by a specific process:
journalctl _PID=1
# show all messages by a specific unit:
journalctl -u <service>
# show kernel ring buffer:
journalctl -k
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NDEzMzQ3NTQsNDQ3ODU1NTU4LC0zOD
k0Mzg5NzUsLTE0MzgxNzEyNDIsLTc2NTU3ODYzNiwtMTgzMDY0
MzA0NCwtMTg5NjM0MDI3NCwxNzE4Nzg2MzY0LDIwOTg5OTIxND
YsLTE4MDQ0ODcxNzUsMTgzNDcwNDk2NywxMTkwMTI5NTkxLDE3
MDI1Nzk3NjIsMTQ1MjQ2NDMyNCwxMzQ0OTI5NjA2LC04ODY3Mj
gzOTQsLTExMjYzMDEwNjQsMTczMzQ4MzM3MiwtMTIxOTMzNTU3
NSwyMjA0NjQ2MjldfQ==
-->