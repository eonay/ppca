#!/bin/bash
#

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.88.111',username='root',password='root')	
ssh.exec_command('poweroff')
ssh.close()

ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect(hostname='192.168.88.222',username='root',password='root')
ssh2.exec_command('poweroff')
ssh2.close()
