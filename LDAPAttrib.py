#Easily view and modify LDAP Attributes

from ldap3 import Connection, Server, SUBTREE, MODIFY_REPLACE
import getpass
import argparse

parser = argparse.ArgumentParser()
#Add server name or IP argument
parser.add_argument("-dc-ip", "--domaincontroller", type=str, help="Server name or IP of Domain Controller.")
#Add port argument
parser.add_argument("--port", type=int, help="Port for LDAP.")
#Add use ssl argument
parser.add_argument("-s", "--ssl", action="store_true", help="Enable SSL. Default: False")
#Add user argument
parser.add_argument("-u", "--user", type=str, help="Username to authenticate with. Format: DOMAIN\\Username")
#Add password argument
parser.add_argument("-p", "--password", type=str, help="Password for username.")
#Add Distinguished Name argument
parser.add_argument("-dn", "--distinguishedname", type=str, help="Distinguished name of object to read or modify.")
#Add Custom baseDN
parser.add_argument("-b", "--basedn", type=str, help="Define base Distinguished Name.")
#Add Attribute argument
parser.add_argument("-a", "--attrib", type=str, help="Attribute to modify or read.")
#Add attribute value argument
parser.add_argument("-v", "--value", type=str, help="Value to give attribute.")
#Add Read argument
parser.add_argument("-r", "--read",  action="store_false", help="Read an attribute. Default Setting")
#Add Modify argument
parser.add_argument("-m", "--modify", action="store_true", help="Modify an attribute.")
#Add custom LDAP filter argument
parser.add_argument("-f", "--filter", type=str, help="Define LDAP filter.")
#Add query ms-DS-MachineAccountQuota
parser.add_argument("-maq", "--MachineAccountQuota", action="store_true", help="Query ms-DS-MachineAccountQuota attribute. Requires BaseDN to be defined.")

args = parser.parse_args()

#If username was defined and password was not prompt for password
if args.user is not None and args.password == None:
    args.password = getpass.getpass()

#Make LDAP Connection
server = Server(args.domaincontroller, port = args.port, use_ssl = args.ssl)
connection = Connection(server, user = args.user, password = args.password, authentication='NTLM')
connection.bind()

connectedas = connection.extend.standard.who_am_i()

#Check if connection was successful
if connectedas != None:
    print("Connected as " + connectedas)
else:
    print("Failed to connect to " + args.domaincontroller +" as " + args.user)
    exit

if args.MachineAccountQuota:
    if not args.basedn:
        print("Missing BaseDN")
        exit
    args.attrib = "ms-DS-MachineAccountQuota"
    args.filter = "(objectClass=Domain)"

if args.modify:
    #Modify and check if was successful
    if connection.modify(args.distinguishedname,{args.attrib: [(MODIFY_REPLACE, [args.value])]}):
        print("Successfully modified " + args.distinguishedname + " attribute " + args.attrib + " to " + args.value)
    else:
        print("Failed to modify " + args.distinguishedname + " attribute " + args.attrib + " to " + args.value)
else:
    if not args.basedn:
        print("Missing BaseDN")
    if not args.filter:
        print("Missing Filter")

    connection.search(search_base = args.basedn, search_scope = SUBTREE, search_filter = args.filter, attributes = [args.attrib])
    print(connection.entries)
