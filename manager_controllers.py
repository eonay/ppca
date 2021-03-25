#!/usr/bin/python3
#
import os

import paramiko

controller1='172.16.187.129'
controller2='172.16.187.130'


def start(controller):
    try :
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=controller,username='root',password='root')
        client.close()
        return True
    except Exception as e:
        return False
        
        

def disponivel(controller):
    response = os.system("ping -c 1 " + controller)
    if response == 0:
        ping_status = True
    else:
        pings_tatus = False
    return ping_status



def start_controllers():
	ssh1 = paramiko.SSHClient()
	ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh1.connect(hostname=controller1,username='root',password='root')
	ssh1.exec_command('kldload carp')
	ssh1.exec_command('sysctl -w net.inet.carp.ifdown_demotion_factor=240')
	ssh1.exec_command('sysctl -w net.inet.carp.senderr_demotion_factor=240')
	ssh1.exec_command('sysctl -w net.inet.carp.demotion=0')
	ssh1.exec_command('sysctl -w net.inet.carp.log=1')
	ssh1.exec_command('sysctl -w net.inet.carp.preempt=1')
	ssh1.exec_command('sysctl -w net.inet.carp.dscp=56') 
	ssh1.exec_command('sysctl -w net.inet.carp.allow=1')
	ssh1.exec_command('ifconfig em0 inet vhid 1 advskew 5 pass senhasecreta alias 10.0.0.1 up')
	ssh1.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
	ssh1.close()

	ssh2 = paramiko.SSHClient()
	ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh2.connect(hostname=controller2,username='root',password='root')
	ssh2.exec_command('kldload carp')
	ssh2.exec_command('sysctl -w net.inet.carp.ifdown_demotion_factor=240')
	ssh2.exec_command('sysctl -w net.inet.carp.senderr_demotion_factor=240')
	ssh2.exec_command('sysctl -w net.inet.carp.demotion=0')
	ssh2.exec_command('sysctl -w net.inet.carp.log=1')
	ssh2.exec_command('sysctl -w net.inet.carp.preempt=1')
	ssh2.exec_command('sysctl -w net.inet.carp.dscp=56') 
	ssh2.exec_command('sysctl -w net.inet.carp.allow=1')
	ssh2.exec_command('ifconfig em0 inet vhid 1 advskew 5 pass senhasecreta alias 10.0.0.1 up')
	ssh2.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
	ssh2.close()


def stop_controllers():
	ssh1 = paramiko.SSHClient()
	ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh1.connect(hostname=controller1,username='root',password='root')
	ssh1.exec_command('sysctl -w net.inet.carp.ifdown_demotion_factor=240')
	ssh1.exec_command('sysctl -w net.inet.carp.senderr_demotion_factor=240')
	ssh1.exec_command('sysctl -w net.inet.carp.demotion=0')
	ssh1.exec_command('sysctl -w net.inet.carp.log=1')
	ssh1.exec_command('sysctl -w net.inet.carp.preempt=0')
	ssh1.exec_command('sysctl -w net.inet.carp.dscp=56') 
	ssh1.exec_command('sysctl -w net.inet.carp.allow=1')
	ssh1.exec_command('ifconfig em0 inet 10.0.0.1 delete')
	#ssh1.exec_command("ps -auxf | egrep ryu-manager | awk '{print $2}' | sed '2d' >> ps-ryu.tmp")
	#ssh1.exec_command("pkill -F ps-ryu.tmp")
	#ssh1.exec_command("rm ps-ryu.tmp")
	ssh1.exec_command("pkill python")
	ssh1.close()
	print('Controller [1]. Stoping ....')
	print('[OK]')

	ssh2 = paramiko.SSHClient()
	ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh2.connect(hostname=controller2,username='root',password='root')
	ssh2.exec_command('sysctl -w net.inet.carp.ifdown_demotion_factor=240')
	ssh2.exec_command('sysctl -w net.inet.carp.senderr_demotion_factor=240')
	ssh2.exec_command('sysctl -w net.inet.carp.demotion=0')
	ssh2.exec_command('sysctl -w net.inet.carp.log=1')
	ssh2.exec_command('sysctl -w net.inet.carp.preempt=0')
	ssh2.exec_command('sysctl -w net.inet.carp.dscp=56') 
	ssh2.exec_command('sysctl -w net.inet.carp.allow=1')
	ssh2.exec_command('ifconfig em0 inet 10.0.0.1 delete')
	#ssh2.exec_command("ps -auxf | egrep ryu-manager | awk '{print $2}' | sed '2d' >> ps-ryu.tmp")
	#ssh2.exec_command("pkill -F ps-ryu.tmp")
	#ssh2.exec_command("rm ps-ryu.tmp")
	ssh2.exec_command("pkill python")
	ssh2.close()
	print('Controller [2]. Stoping ....')
	print('[OK]')
	
	
def status_controllers():
	#ifconfig em0 | egrep vhid	
	pass
	
	

def boot_controller(controller):
	ssh1 = paramiko.SSHClient()
	ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh1.connect(hostname=controller,username='root',password='root')
	ssh1.exec_command('kldload carp')
	ssh1.exec_command('sysctl -w net.inet.carp.ifdown_demotion_factor=240')
	ssh1.exec_command('sysctl -w net.inet.carp.senderr_demotion_factor=240')
	ssh1.exec_command('sysctl -w net.inet.carp.demotion=0')
	ssh1.exec_command('sysctl -w net.inet.carp.log=1')
	ssh1.exec_command('sysctl -w net.inet.carp.preempt=1')
	ssh1.exec_command('sysctl -w net.inet.carp.dscp=56') 
	ssh1.exec_command('sysctl -w net.inet.carp.allow=1')
	ssh1.exec_command('ifconfig em0 inet vhid 1 advskew 5 pass senhasecreta alias 10.0.0.1 up')
	ssh1.exec_command('nohup ryu-manager /usr/local/lib/python3.7/site-packages/ryu/app/simple_switch.py &')
	ssh1.close()



def drop_controller(controller):
	ssh1 = paramiko.SSHClient()
	ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh1.connect(hostname=controller,username='root',password='root')
	ssh1.exec_command('sysctl -w net.inet.carp.ifdown_demotion_factor=240')
	ssh1.exec_command('sysctl -w net.inet.carp.senderr_demotion_factor=240')
	ssh1.exec_command('sysctl -w net.inet.carp.demotion=0')
	ssh1.exec_command('sysctl -w net.inet.carp.log=1')
	ssh1.exec_command('sysctl -w net.inet.carp.preempt=0')
	ssh1.exec_command('sysctl -w net.inet.carp.dscp=56') 
	ssh1.exec_command('sysctl -w net.inet.carp.allow=1')
	ssh1.exec_command('ifconfig em0 inet 10.0.0.1 delete')
	#ssh1.exec_command("ps -auxf | egrep ryu-manager | awk '{print $2}' | sed '2d' >> ps-ryu.tmp")
	#ssh1.exec_command("pkill -F ps-ryu.tmp")
	#ssh1.exec_command("rm ps-ryu.tmp")
	ssh1.exec_command("pkill python")
	ssh1.close()
	print('Controller [1]. Stoping ....')
	print('[OK]')



