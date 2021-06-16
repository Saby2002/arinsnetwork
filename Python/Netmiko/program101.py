#!/usr/bin/env python

from pprint import pprint
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

def send_show_command(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output

        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)

if __name__ == "__main__":
    device = {
            "device_type": "cisco_ios_ssh",
            "host": "169.254.255.101",
            "username": "saby",
            "password": "saby",
            "secret" : "saby",
    }
    result = send_show_command(device, ["show arp", "show ip int br"])
    pprint(result, width=120)


