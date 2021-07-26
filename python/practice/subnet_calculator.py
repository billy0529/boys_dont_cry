## subnet calculator rev 1.0
## Author: billy.han@exanetix.com
## Modules
import sys

## Global Vars
ip_addr = []

## Questionaires
while True:
    print("\n<<< Subnet Calculator Rev 1.0 >>>")
    ip_addr.append(input("<<< Please type IP address (x.x.x.x): "))
    ip_addr.append(input("<<< Please type Subnet Mask (/x or xxx.xxx.xxx.xxx): "))
    print("\nPlease check the information you type:")
    print("\nIP ADDRESS: {0}".format(ip_addr[0]))
    print("SUBNET MASK: {0}".format(ip_addr[1]))
    ans1 = input("\nIs this information correct? (y/n): ")
    if ans1 == "y": break
    
ip_addr[0] = 9
print(ip_addr)

