## Module Netmiko

Netmiko is a module that makes t easier to use paramiko for network device. 
Netmiko used paramiko but also creates interface and methods needed to work with network devices

First need to install netmiko
It uses dictionary for defining device parameters
Dictionary may have then next parameters

# Sending Commands 

Netmiko has several ways to send commands 
- send_command = send one command
- send_config_set = send list of commands or command in configuration mode
- send_conf_from_file = send commands from the file (uses send_config_set method in-side)
- send_command_timing = send command and wait for the output based on timer

# Method works as follows : 

- sends command to device and gets the output until string with prompt or until specified string 
	- prompt is automatically determined
	- if your device does not determine it, you can simply specify a string till which to read the output. 
	- send_command_expect method previously worked this way, but since version 1.0.0 this is how send_command works and send_command_except method is left for compatibility
	
	- Following parameters can be passed to method:

		- command_string = command
		- expect_string = to which substring to read the output
		- delay_factor = option allows to increase delay before the start of string search
		- max_loops = number of iterations before method gives out an erro (exception). By default 500
		- strip_command = remove command from output

# Send_config_set

- Method send_conf_set allows you to send command or multiple commands in configuration mode.

Example : 

commands = ['router ospf 1',
	    'network 9.1.2.0 255.255.255.0 area 0',
	    'network 9.1.4.0 255.255.255.0 area 0',
	    'network 101.101.101.101 255.255.255.255 area 0']


