#!/usr/bin/python

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.219.111',username='root',password='root')
#ssh.exec_command("ps -auxf | egrep ryu-manager | awk '{print $2}' | sed '2d' >> ps-ryu.tmp")
#ssh.exec_command("pkill -F ps-ryu.tmp")
ssh.exec_command("pkill python")
#ssh.exec_command("rm ps-ryu.tmp")
ssh.close()
print('...')

ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect(hostname='192.168.219.222',username='root',password='root')
#ssh2.exec_command("ps -auxf | egrep ryu-manager | awk '{print $2}' | sed '2d' >> ps-ryu.tmp")
#ssh2.exec_command("pkill -F ps-ryu.tmp")
ssh2.exec_command("pkill python")
#ssh2.exec_command("rm ps-ryu.tmp")
ssh2.close()
print('...')
