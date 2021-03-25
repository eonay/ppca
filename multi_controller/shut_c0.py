#!/bin/bash
#

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.219.111',username='root',password='root')	
ssh.exec_command('poweroff')
ssh.close()

