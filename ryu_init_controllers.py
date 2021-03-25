import os
import time
import paramiko
#hostname = "192.168.88.111"
#response = os.system("ping -c 1 " + hostname)

status = False
login = 'root'
senha = 'senha'
#espera = 15
espera = 4
c1 = '192.168.219.111' 
c2 = '192.168.219.222'

c1_status = False
c2_status = False

'''

while True:

	if response == 0:
	  print (hostname, 'is up!')
	else:
	  print (hostname, 'is down!')

	time.sleep(espera)
'''

def start(controller):
    try :
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=controller,username='root',password='root')
        #client.close()
        return True
    except Exception as e:
        #client.close()
        #print(e)
        return False


#print(start('192.168.88.111'))


def disponivel(controller):
    #hostname = "192.168.88.111"
    response = os.system("ping -c 1 " + controller)

    if response == 0:
        pingstatus = True
    else:
        pingstatus = False

    return pingstatus

#print(disponivel('192.168.88.111'))

while True:
	print('################# Off #################')

	while start(c1):
		key = False
		print('################# C1 On #################')
		conn = paramiko.SSHClient()
		conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		conn.connect(hostname='192.168.219.111',username='root',password='root')
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
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname='192.168.219.111',username='root',password='root')
			ssh.exec_command('kldload carp')
			ssh.exec_command('ifconfig em0 inet vhid 1 advskew 55 pass senhasecreta alias 192.168.219.123/32 up')
			ssh.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
			ssh.close()
			time.sleep(espera)
		time.sleep(espera)






		while start(c2):
			key = False
			print('################# C2 On #################')
			conn = paramiko.SSHClient()
			conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			conn.connect(hostname='192.168.219.222',username='root',password='root')
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
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh.connect(hostname='192.168.219.222',username='root',password='root')
				ssh.exec_command('kldload carp')
				ssh.exec_command('ifconfig em0 inet vhid 1 advskew 22 pass senhasecreta alias 192.168.219.123/32 up')
				ssh.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
				ssh.close()
				time.sleep(espera)
			time.sleep(espera)

'''
			Key = True
		
		time.sleep(espera)
		while key:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname='192.168.88.111',username='root',password='root')
			ssh.exec_command('kldload carp')
			ssh.exec_command('ifconfig em0 inet vhid 1 advskew 55 pass senhasecreta alias 192.168.88.123/32 up')
			ssh.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
			ssh.close()

			key = False



'''
'''
while True:

	if disponivel(c1) == True:
		time.sleep(1)
		print (c1, 'is up runing!')
		time.sleep(1)
		if c1_status:
			print('################# LIGADO (#################')
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname='192.168.88.111',username='root',password='root')
			#ssh.exec_command("ifconfig | egrep carp | awk '{print $1}'")
			
			stdin, stdout, stderr = ssh.exec_command("ifconfig | egrep carp | awk '{print $1}'")
			#stdin.write('1234\n')
			stdin.flush()
			ifv = stdout.readlines()
			print(ifv[0])

			if ifv[0] == 'carp:\n':
				print('tudo certo')
			else:
				c1_status = False

			#stdin, stdout, stderr = ssh.exec_command("uptimeee")
			#stdin, stdout, stderr = ssh.exec_command("ifconfig | egrep carp | awk '{print $1}'")
			#print (stdout.channel.recv_exit_status())

			time.sleep(1)



		else:
			if disponivel(c1) == True:
				ssh = paramiko.SSHClient()
				time.sleep(1)
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				time.sleep(1)
				ssh.connect(hostname='192.168.88.111',username='root',password='root')
				ssh.exec_command('kldload carp')
				ssh.exec_command('ifconfig em0 inet vhid 1 advskew 55 pass senhasecreta alias 192.168.88.123/32 up')
				ssh.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
				ssh.close()
				if ssh:
					print('controller reconfig...')
					print('[OK]')
					c1_status = True
			else:
				c1_status = False

		time.sleep(espera)
	else:
		print (c1, 'is down, problema!')
		c1_status = False

'''