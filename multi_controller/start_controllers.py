#!/usr/bin/python

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.219.111',username='root',password='root')	
ssh.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
ssh.close()
print('...')
ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect(hostname='192.168.219.222',username='root',password='root')
ssh2.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
ssh2.close()
print('...')
