import time
import paramiko



#使用invoke进行交互操作http://blog.chinaunix.net/uid-28841896-id-4812715.html
def Verification_ssh(host,username,password,port):
    s=paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(host+username+password)
    s.connect(hostname = host,port=port,username=username, password=password)
    return s
