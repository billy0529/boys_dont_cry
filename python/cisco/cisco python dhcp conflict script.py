### Python 3.0

import sys
import getpass
import telnetlib

HOST1 = "203.235.23.***"
user = input("Please Enter valid username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST1)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")

tn.write(b"clear ip dhcp conflict *\n")    ### cisco delete DHCP conflict entry
tn.write(b"exit\n")      ### if no exit, wait until connection timeout

print(tn.read_all().decode('ascii'))      ### print typed scripts


