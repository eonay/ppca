#
import os

import paramiko
from scp import SCPClient

controller1='172.16.187.129'
controller2='172.16.187.130'

print('***Controller[1]...')
ssh1 = paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh1.connect(hostname=controller1,username='root',password='root')	
ssh1.exec_command('nohup vmstat 1 220 >> c1-cpu_memory-v1.out &')
os.system('sh run_cbench.sh c1')
with SCPClient(ssh1.get_transport()) as scp:
    scp.get('/root/c1-cpu_memory-v1.out')
ssh1.close()
print('[OK]')


print('***Controller[2]...')
ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect(hostname=controller2,username='root',password='root')	
ssh2.exec_command('nohup vmstat 1 220 >> c2-cpu_memory-v1.out &')
os.system('sh run_cbench.sh c2')
with SCPClient(ssh2.get_transport()) as scp:
    scp.get('/root/c2-cpu_memory-v1.out')
ssh2.close()
print('[OK]')

os.system('sudo chmod 777 *')

