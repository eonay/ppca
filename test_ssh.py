import paramiko



def start():
    try :
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname='192.168.88.111',username='root',password='root')
        return True
    except Exception as e:
        #client.close()
        #print(e)
        return False

