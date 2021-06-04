from netmiko import ConnectHandler
from netmiko.cisco import CiscoIosSSH, CiscoIosTelnet

osma = {
    'device_type': 'cisco_ios',
    'host': '203.231.96.58',
    'username': '=billyne=',
    'password': '!!GGkswodls61'
}
net_connect = ConnectHandler(**osma)
commands = ['interface g3/19',
            'description TESTSSH-2']
result = net_connect.send_config_set(commands)
print(result)

