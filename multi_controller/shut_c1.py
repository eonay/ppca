#!/bin/bash
#

import paramiko


ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect(hostname='192.168.219.222',username='root',password='root')
ssh2.exec_command('poweroff')
ssh2.close()
