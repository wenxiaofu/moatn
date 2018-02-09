import time
import paramiko
from poll.mfunc.ctestu import *
from poll.mfunc.caseroutec import Caseroutec
import json
import re
from poll.mfunc.caserun import Caserun
import os,django


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
        result = stdout.read().decode('utf-8') #不加decode会显示成bety字符，这里需要转一下
        print(result)
        s.close()
    return result

if __name__ == "__main__":
    print("ddd")
   # verification_ssh('200.200.169.212', 'root', 'moatest', 22, 'OrYuWFHeLDBtgX1BitJu',
     #                'mdbg -p 21024 -o exportdomain;ifconfig;cd /home/testHealth;./testHealth.sh')
    '''
    re = GetSrv('200.200.169.212','root','moatest')
    list = re.split("\n") #先用换行符进行一次分隔
    #第一个不需要
    count = len(list)-1
    lastlist = []
    for i in range(len(list)-1):
        lists = list[i].split()
        lists.insert(0,i) #增加一个id
        #转换成一个json
        #先都转换成字典
        data =  {}
        data["srvcode"] = lists[2]
        data["srvdec"] = lists[3]
        data["srvname"] = lists[1]
        data["id"] = lists[0]
        #组合到一个数组里面
        lastlist.append(data)

        # print(lists)
        print(data)
    data = {}
    data["srv"] = lastlist
    print(data)
    jsondata = json.dumps(data)
    print(jsondata)
    print(list)
    print(lastlist)
    print(len(lastlist))
'''
    # print(GetSrv('200.200.169.212','root','moatest'))
    #print(GetInterface('200.200.169.212','root','moatest','0x39'))
    '''
    result = GetModel('200.200.169.212', 'root', 'moatest', '0x3901')
    find_list = re.findall(r"Req(.*)",result)
    a = find_list[0]
    print(a)
'''
    # print(SenYeWu('200.200.169.212', 'root', 'moatest','23728632463','12345','0x3901', '{"workreport":{"wrdate" : 1502035200000,"Type":1,"content":"1221212112"}}'))
    # print(SenYeWu('200.200.169.212', 'root', 'moatest', '23728632463', '12345', '0x3901',
    #               '{"workreport":{"wrdate" : 1502035200000,"Type":1,"content":"1221212112"}}'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poll.settings")  # project_name 项目名称
    django.setup()
    Caserun(3)