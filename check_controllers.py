import time

import paramiko

import manager_controllers

espera=2
controller1='172.16.187.129'
controller2='172.16.187.130'

while True:
	print('################# Off #################')
	
	if manager_controllers.start(controller1):
		key = False
		print('################# C1 On #################')
		conn = paramiko.SSHClient()
		conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		conn.connect(hostname=controller1,username='root',password='root')
		stdin, stdout, stderr = conn.exec_command("ifconfig | egrep carp | awk '{print $1}'")
		stdin.flush()
		ifv = stdout.readlines()
		if ifv:
			time.sleep(espera)
			conn.close()
		else:
			manager_controllers.boot_controller(controller1)
			'''
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname=controller1,username='root',password='root')
			ssh.exec_command('kldload carp')
			ssh.exec_command('ifconfig em0 inet vhid 1 advskew 55 pass senhasecreta alias 10.0.0.1/32 up')
			ssh.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
			ssh.close()
			'''
			time.sleep(espera)
		time.sleep(espera)



	if manager_controllers.start(controller2):
		key = False
		print('################# C2 On #################')
		conn = paramiko.SSHClient()
		conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		conn.connect(hostname=controller2,username='root',password='root')
		#ssh.exec_command("ifconfig | egrep carp | awk '{print $1}'")
		
		stdin, stdout, stderr = conn.exec_command("ifconfig | egrep carp | awk '{print $1}'")
		#stdin.write('1234\n')
		stdin.flush()
		ifv = stdout.readlines()
		#print(ifv[0])

		#if ifv[0] == 'carp:\n':
		if ifv:
			#print('tudo certo')
			time.sleep(espera)
			conn.close()

		else:
			manager_controllers.boot_controller(controller2)
			'''
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname=controller2,username='root',password='root')
			ssh.exec_command('kldload carp')
			ssh.exec_command('ifconfig em0 inet vhid 1 advskew 22 pass senhasecreta alias 10.0.0.1/32 up')
			ssh.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
			ssh.close()
			'''
			time.sleep(espera)
		time.sleep(espera)


