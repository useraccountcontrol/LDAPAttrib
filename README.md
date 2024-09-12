Description
-----------
LDAPAttrib is a tool to read and modify LDAP attributes.

Usage
-----
usage: LDAPAttrib.py [-h] [-dc-ip DOMAINCONTROLLER] [--port PORT] [-s] [-u USER] [-p PASSWORD] [-dn DISTINGUISHEDNAME] [-b BASEDN] [-a ATTRIB] [-v VALUE] [-r] [-m]
                     [-f FILTER] [-maq]

 options:

-h, --help            show this help message and exit
 
-dc-ip DOMAINCONTROLLER, --domaincontroller DOMAINCONTROLLER Server name or IP of Domain Controller.

--port PORT           Port for LDAP.

-s, --ssl             Enable SSL. Default: False

-u USER, --user USER  Username to authenticate with. Format: DOMAIN\Username

-p PASSWORD, --password PASSWORD   Password for username.

-dn DISTINGUISHEDNAME, --distinguishedname DISTINGUISHEDNAME  Distinguished name of object to read or modify.

-b BASEDN, --basedn BASEDN  Define base Distinguished Name.

-a ATTRIB, --attrib ATTRIB Attribute to modify or read.

-v VALUE, --value VALUE Value to give attribute.

-r, --read Read an attribute. Default Setting

-m, --modify Modify an attribute.

-f FILTER, --filter FILTER  Define LDAP filter.

-maq, --MachineAccountQuota Query ms-DS-MachineAccountQuota attribute. Requires BaseDN to be defined.

Examples
--------

**Read an attribute**

`LDAPAttrib.py -dc-ip 192.168.57.13 -r --basedn BASE DISTINGUISHED NAME -f '(FILTER)' -a ATTRIBUTE -u DOMAIN\USERNAME`
![image](https://github.com/user-attachments/assets/4bd1f137-1bac-4b78-9823-29ccdb8e64d1)

**Modify an attribute**

`LDAPAttrib.py -dc-ip DOMAIN CONTROLLER -m -dn DISTINGUISHED NAME -a ATTRIBUTE --value VALUE -u DOMAIN\USERNAME`
![image](https://github.com/user-attachments/assets/8d299da6-6976-47f5-b451-993b6c5a260a)

**Reading ms-DS-Machine-Account-Quota**

`LDAPAttrib.py -dc-ip DOMAIN CONTROLLER --basedn BASE DISINGUISHED NAME -maq -u DOMAIN\USERNAME`
![image](https://github.com/user-attachments/assets/969050bd-7f24-4a9c-b71f-c0f84ed5a09e)

