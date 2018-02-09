#对服务端ctest工具的调用，用于接口测试
#主要功能：图形化ctest的使用，完成接口调用
#一次连接就可以一直使用，不需要重复连接，一个web进程来控制

import time
import paramiko
import json
import re
import socket

#创建ssh连接
def Verification_ssh(host,username,password):
    s=paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(host+username+password)
    s.connect(hostname = host,username=username, password=password,timeout=10)
    return s

#发送命令
def sendCmd(host,username,password,cmd):
    try:
        s = Verification_ssh(host,username,password)
        print(s)
        print("adadddddddddddddddddd"+cmd)
        stdin, stdout, stderr = s.exec_command(cmd,timeout=6)
        result = stdout.read().decode('utf-8') #不加decode会显示成bety字符，这里需要转一下
        return result
       # print(result)
        print(s.close()+"ddddddddd")
    except socket.timeout:
        print("超时了")
        return "注意：执行命令超时6s，请手动执行一下"
       #print(s.close())
        s.close()
    except ConnectionAbortedError:
        s.close()
#发送批量命令
def sendCmds(host,username,password,*cmds):
    s = Verification_ssh(host,username,password)
    result = ""
    for i in cmds:
        stdin, stdout, stderr = s.exec_command(i)
    # result = stdout.read().decode('utf-8') #不加decode会显示成bety字符，这里需要转一下
        result = stdout.read() + result
        return result
   # print(result)
    s.close()



#拼接ctest的cmd

#获取模块
def GetSrv(host,username,password):
    cmd = 'ctest -srv'
    result = sendCmd(host,username,password,cmd)
    list = result.split("\n")  # 先用换行符进行一次分隔
    count = len(list) - 1
    lastlist = []
    for i in range(len(list) - 1):
        lists = list[i].split()
        lists.insert(0, i)  # 增加一个id
        # 转换成一个json
        # 先都转换成字典
        data = {}
        data["srvcode"] = lists[2]
        data["srvdec"] = lists[3]
        data["srvname"] = lists[1]
        data["id"] = lists[0]
        # 组合到一个数组里面
        lastlist.append(data)
    data = {}
    data["srv"] = lastlist
    print(data)
    jsondata = json.dumps(data)
    return str(jsondata)

#获取接口
def GetInterface(host,username,password,module):
    interface = 'ctest -srv '+ module
    print(interface)
    result = sendCmd(host,username,password,interface)
    list = result.split("\n")  # 先用换行符进行一次分隔
    # 第一个不需要
    del list[0]
    count = len(list) - 1
    lastlist = []
    for i in range(len(list) - 1):
        lists = list[i].split()
        lists.insert(0, i)  # 增加一个id
        # 转换成一个json
        # 先都转换成字典
        data = {}
        data["srvcode"] = lists[2]
        data["srvdec"] = lists[3]
        data["srvname"] = lists[1]
        data["id"] = lists[0]
        # 组合到一个数组里面
        lastlist.append(data)
    data = {}
    data["srv"] = lastlist
    print(data)
    jsondata = json.dumps(data)
    return str(jsondata)

#获取json模板,这个模板还可以优化，通过解析pb文件获取，但是非常麻烦，暂时没有这个必要
def GetModel(host,username,password,interface):
    jsonModel = 'ctest -s ' + interface + ' -h'
    print(jsonModel)
    result = sendCmd(host,username,password,jsonModel)
    #re模块还没有怎么用，先这样用一下了
    find_list = re.findall(r"Req(.*)", result)
    a = find_list[0]
    return a

#登陆发送业务请求
def SenYeWu(host,username,password,phone,pwd,interface,jsondata):
    jsonstr = 'ctest -u '+ phone + ' -p '+ pwd + ' -s ' + interface + ' -j \''+ jsondata +'\''+' -PB_PRINT'
    print(jsonstr)
    result = sendCmd(host,username,password,jsonstr)
    return result
'''
传入json
登陆测试，不登陆测试
返回数据
增加检验返回结果

'''
#def ctest(json,srvid,)


