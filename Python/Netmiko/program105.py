#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

XR1 = {
        "host" :'169.254.255.103',
        "username" : 'saby',
        "password" : getpass(),
        "device_type" : "cisco_xr",
}

connect = ConnectHandler(**XR1)

output = connect.send_command("show version")

with open("show_version_xr", "w") as f:
    f.write(output)
    
