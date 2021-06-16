#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass


connect = ConnectHandler(host='169.254.255.101',
                         username='saby',
                         password=getpass(),
                         device_type='cisco_ios',
                        # session_log='IOS_VERSION.txt',
)



output = connect.send_command('show version')

with open("show_version.txt", "w") as f:
    f.write(output)


connect.disconnect()



