import sys
import getpass
import telnetlib

IPRANGE = "172.1.1."
IPRANGE = "192.168.90." 

user = input("Please Enter valid username: ")
password = getpass.getpass()

DEVICE = 0
while DEVICE < 20:
    DEVICE = DEVICE + 1
    HOST = IPRANGE + str(DEVICE)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"username billy pri 15 pass gkswodls61\n")
    tn.write(b"configuration terminal\n")
    tn.write(b"username billy privilage 15 password gkswodls61\n")
    tn.write(b"no ip domain-lookup\n")
    tn.write(b"service password-encryption\n")
    tn.write(b"interface g5\n")
    tn.write(b"des [MANAGEMENT IP ASSIGNED]\n")
    tn.write(b"description [MANAGEMENT IP ASSIGNED]\n")
    tn.write(b"exit\n")
    tn.write(b"line vty 0 4\n")
    tn.write(b"login local\n")
    tn.write(b"logg sync\n")
    tn.write(b"exec-time 0 0\n")
    tn.write(b"logging synchronous\n")
    tn.write(b"exec-timeout 0 0\n")
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"write memory\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
    if DEVICE == 20:
        print("=== Remote Access Configuration Done! ===")
        print("=== Remote Access Configuration Done! ===")