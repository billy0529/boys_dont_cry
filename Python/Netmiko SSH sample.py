from netmiko import ConnectHandler
from netmiko.cisco import CiscoIosSSH, CiscoIosTelnet

osma = {
    'device_type': 'cisco_ios',
    'host': '103.82.118.1',
    'username': '=billyne=',
    'password': ''
}
net_connect = ConnectHandler(**osma)
output = net_connect.send_command('show int status')
print(output)


