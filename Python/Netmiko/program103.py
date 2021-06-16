#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

connect = ConnectHandler(
        host='169.254.255.104',
        username='admin',
        password=getpass(),
        device_type='nokia_sros',
        session_log='my_session.txt',
)

print(connect.find_prompt)

