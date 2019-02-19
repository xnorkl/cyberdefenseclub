
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
The entire team is responsible for completing each inject. 

If an inject does not directly deal with a service or device under your team's purview or if there are no current injects at all, move to hardening, then enumeration, then hunt. Rinse and repeat.
 
 ```mermaid
graph LR
A(0. Inject) --> B(1. Harden)
B --> C(2. Enumate)
C --> D(3. Hunt)
D --> A
```



## Injects

Injects are most often tasks associated with system administration.
Along with maintaining fundamental services, injects take priority.
/example inject/
It is each team's responsibility to properly resolve an inject tasked by the Captain or Change Control Officer and pass along proper documentation. Ask for help often.

## Hardening
There should be no injects given within the first 15 minutes. 
Hardening each and every device under your purview is the first objective that should be taken.  
 
1. Change Default Credentials
2. Create an Admin Account
4. Restrict Login Access  

### Network Admin 

### Windows Team
log successful and failed logins
```powershell
auditpol.exe /set /category:"Logon/Logoff"  /success:enable /failure:enable | out-null
```

### Linux Team
**Adding an Administrator Account**
```bash
#Change default password for default login
passwd 
#Open a root shell and change root password
su 
passwd
#While root, change default username
usermod -l <newname> <oldname>
usermod -d ~/home/<newname> -m <newname>
ln -s ~/home/<newname> ~/home/<oldname>
#Create an admin account
useradd -mg wheel <admin>
passwd <admin> 
exit
#Login as admin and restrict root and su
sudo -i -u <admin>
sudo passwd -l root
#Always use sudo -i -u <admin> when performing admin tasks!
```
**Administrating the Wheel Group**

Add the wheel group if it doesn't already exist. 
Restrict the use of sudo to the wheel group by configuring **/etc/sudoers**. Use visudo and uncomment the following: 
```bash
wheel ALL=(ALL) ALL  
```
Restrict use of su with pam. 
Uncomment or add the following line to **/etc/pam.d/su**:
```bash
auth		requirement	pam_wheel.so group=wheel
```
**User Administration**
Set a delay upon authentication failure
Lock out a user after 3 repeated failed attempts
```bash
/etc/pam.d/system-login

auth optional pam_faildelay.so delay=4000000
auth required pam_tally2.so deny=3 unlock_time=600 onerr=succeed file=/var/log/tallylog
```
Limit processes run by users
```bash
/etc/security/limits.conf

* soft nproc 100
* hard nproc 200
```



	

## Enumeration


## Hunting

### Windows Team


### Linux Team

#### File Permissions

|              |ASCII                          |HTML                         |
|----------------|-------------------------------|-----------------------------|
|Owner|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Group          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Other          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|
**chmod**
```bash
#
chmod 0077 /boot /etc/{iptables,artptables}
```

**chown**


|                |ASCII                          |HTML                         |
|----------------|-------------------------------|-----------------------------|
|Single backticks|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Quotes          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Dashes          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjIwOTk4MTYxLDIyMDQ2NDYyOSwxNDkzOD
AxODY4LDE3NDYxMzEzMl19
-->