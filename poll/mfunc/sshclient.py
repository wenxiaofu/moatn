import time
import paramiko

#使用invoke进行交互操作http://blog.chinaunix.net/uid-28841896-id-4812715.html
def verification_ssh(host,username,password,port,root_pwd,cmd):
    print(111111111111)
    s=paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(host+username+password)
    s.connect(hostname = host,port=port,username=username, password=password)
    if username != 'root':
        ssh = s.invoke_shell()
        time.sleep(0.1)
        ssh.send('su - \n')
        # time.sleep(2)
        buff = ''
        while (("Password" in buff) == False):
            resp = ssh.recv(999)
            resp1 = str(resp)
            print("-------------" + resp1 + "------------------")
            buff += resp1
            print("Password" in buff)
            print(buff)
        print("lalala ")
        ssh.send(root_pwd)
        ssh.send('\n')
        time.sleep(2)
        buff = ''
        #here is use for test the response
        while (("#" in buff) == False):
            resp = str(ssh.recv(999))
            buff += resp
            print(buff)
        ssh.send(cmd)
        ssh.send('\n')
        #发送命令
        buff = ''
        while (("#" in buff) == False):
            resp = str(ssh.recv(999))
            buff += resp
            print(buff)
        s.close()
        #result = buff
        print("hahahha ")
        result = buff
    else:
        stdin, stdout, stderr = s.exec_command(cmd)

        # result = stdout.read().decode('utf-8') #不加decode会显示成bety字符，这里需要转一下
        result = stdout.read()
        print(result)
        s.close()
    return result
