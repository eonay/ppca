#!/usr/bin/python3
#
#
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.88.111',username='root',password='root')	
ssh.exec_command('reboot')
ssh.close()

