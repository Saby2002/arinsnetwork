#!/usr/bin/env python

import paramiko
import time 
import socket
#from pprint import pprint


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="169.254.255.101",
               username="saby",
               password="saby",
               look_for_keys=False,
               allow_agent=False)
ssh = client.invoke_shell()
ssh.send("enable\n")
time.sleep(2)
ssh.send("show ip int br\n")
time.sleep(2)
ssh.send("show arp\n")
time.sleep(2)
ssh.send("show clock\n")
output = ssh.recv(3000).decode("utf-8")
print(output)

ssh.close()


