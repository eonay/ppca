#
import paramiko
import os
from scp import SCPClient

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.219.111',username='root',password='root')	
ssh.exec_command('nohup vmstat -h 1 150 >> c0-cpu_memory-v1.out &')
###ssh.close()
os.system('sh c0-run_cbench.sh')


with SCPClient(ssh.get_transport()) as scp:
    scp.get('/root/c0-cpu_memory-v1.out')

ssh.close()
#sftp.close()
'''
os.system('scp root@192.168.219.111:/root/cpu_memory.out .')

with SCPClient(ssh.get_transport()) as scp:
    scp.put('test.txt', 'test2.txt')
    scp.get('test2.txt')
'''



ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect(hostname='192.168.219.222',username='root',password='root')	
ssh2.exec_command('nohup vmstat -h 1 150 >> c1-cpu_memory-v1.out &')
###ssh.close()
os.system('sh c1-run_cbench.sh')


with SCPClient(ssh2.get_transport()) as scp:
    scp.get('/root/c1-cpu_memory-v1.out')

ssh2.close()


os.system('sudo chmod 777 *')

