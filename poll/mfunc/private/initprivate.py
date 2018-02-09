import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moat.settings")# project_name 项目名称
django.setup()
from poll.mfunc.ctestu import *
from poll.mfunc.private.PrivateRoute import privateR
from poll.models import Private
import re

def GetPrivates(host, username, password):
    result = sendCmd(host, username, password, "mdbg -i servermap.moa.kdzl.cn -p 21120 -o exportserver|grep is_private_cloud\(1\)")
    return result

def init(host, username, password):
    result =  sendCmd(host, username, password, "mdbg -i servermap.moa.kdzl.cn -p 21120 -o exportserver|grep is_private_cloud\(1\)")
    list = result.split("\n")
    for i in range(len(list) - 1):
        print(list[i])
        pr =  Private()

        #提取
        # 提取状态
        status = re.findall(r"status\((.+?)\)", list[i])
        status = status[0]
        pr.status = status
        # 提取srvid
        srvid = re.findall(r"id\((.+?)\)", list[i])
        srvid = srvid[0]
        #加个判断，先判断数据库里面
        pr.srv_id = int(srvid)
        # 提取entryip
        entryip = re.findall(r"pc_entryip\((.+?)\)", list[i])
        entryip = entryip[0]
        if ("pc_entryip()" in list[i]):
            entryip = ""
        pr.pc_ip = entryip
        #提取名字
        name = re.findall(r"name\((.+?)\)", list[i])
        name = name[0]
        if ("name()" in list[i]):
            name = ""
        pr.name = name
        #测试账号
        tsname = "100"+srvid+"11111"
        pwd = "admin123"
        pr.testAdmin = tsname
        pr.testAdminpwd = pwd
        pr.mdbgrsp = list[i]
        pr.save()

if __name__ == "__main__":
    p = privateR()
    p.GetInstalledPrivate()
    #result = init("200.200.169.100", "root", "OrYuWFHeLDBtgX1BitJu")
    '''
    print("begin")
    result=GetPrivates("200.200.169.100","root","OrYuWFHeLDBtgX1BitJu")
    #开始提取;srvid;entry_ip,是否有同步通讯录，响应结果保存到数据库，可以点击查看详情查看
    list = result.split("\n")
    for i in range(len(list) - 1):
        print(list[i])
        srvmap_server[status(INIT), id(154), ip(200.200
        .169
        .100), users(0), domains(0), enable(1), is_beta(0), is_private_cloud(1), name(), pc_entryip(), adr(0), wdr(0)]
        #提取状态
        status =  re.findall(r"status\((.+?)\)", list[i])
        status = status[0]
        #提取srvid
        srvid = re.findall(r"id\((.+?)\)", list[i])
        srvid = srvid[0]
        #提取entryip
        entryip = re.findall(r"pc_entryip\((.+?)\)", list[i])
        entryip = entryip[0]
        if(entryip == "),adr(0"):
            entryip = ""
        print(status+srvid+entryip)
'''