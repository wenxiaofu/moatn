from poll.models import Private
from poll.mfunc.ctestu import *
from django.utils import timezone
import re

class privateR():
    cloudip = "200.200.169.100"
    username = "root"
    pwd = "OrYuWFHeLDBtgX1BitJu"
    def Regprivate(self,deadline,num,sync,installway,privateip,port,eth,name):
        cloudip = self.cloudip
        username = self.username
        pwd = self.pwd
        cmd = "tool_addsrv_private -o add_server 'is_private_cloud=1' -l "+str(num)+" -e "+str(deadline)+""
        print(cmd)
        result = sendCmd(cloudip,username,pwd,cmd)
        print(result)
        srvid = re.findall(r"srvid=(.+?)\n", result)
        srvid = srvid[0].strip()
        print(srvid)
        password = re.findall(r"password=(.+?)\n", result)
        password = password[0]
        if(sync == "1"):
            print("不需要同步通讯录")
            if(installway == "1" ):
                print("使用ip,有外网ip，不需要输入端口6802")
                installstr = "./toolInstallPocketPrivate.sh -s "+srvid+" -p "+password+" -i "+privateip+" -e "+eth+" -n "+name
            elif(installway == "2" ):
                print("使用端口号，不需要使用ip")
                installstr = "./toolInstallPocketPrivate.sh -s " + srvid + " -p " + password + " -P " + port + " -e " + eth + " -n " + name
        elif(sync== "0"):
            if (installway == "1"):
                print("使用ip,有外网ip，不需要输入端口6802")
                installstr = "./toolInstallPocketPrivate.sh -s " + srvid + " -p " + password + " -i " + privateip + " -e " + eth + " -n " + name +" -r 0"
            elif (installway == "2"):
                print("使用端口号，不需要使用ip")
                installstr = "./toolInstallPocketPrivate.sh -s " + srvid + " -p " + password + " -P " + port + " -e " + eth + " -n " + name +" -r 0"
        else:
            installstr = "传入的sync参数不对，查一下原因"
        #生成安装命令
        print(installstr)
        pv = Private()
        result = result +"\n 安装命令为：\n"+ installstr
        print("-----------------------------")
        print(result)
        pv.srv_id = int(srvid)
        pv.regresult = result
        pv.save()
        print(result)
        return result
    #接收一个json 对象
    def Editprivate(self,jdata):
        try:
            pr = Private.objects.filter(srv_id=jdata["data"]["srv_id"]).update(name=jdata["data"]["name"], num=jdata["data"]["num"],
                                                                          asyncphone=int(jdata["data"]["asyncphone"]), pc_ip=jdata["data"]["pc_ip"],
            is_lan=jdata["data"]["is_lan"],other=jdata["data"]["other"],begin_time=jdata["data"]["begin_time"],end_time=jdata["data"]["end_time"])
            return "保存成功"
        except KeyError as e:
            return e


    def Getdetail(self,srvid):
        latest_question_list = Private.objects.filter(srv_id=srvid).values("srv_id","name","status","pc_ip","asyncphone",
                               "is_lan","begin_time","end_time","num","adminUser","testAdmin","testAdminpwd",
                               "mdbgrsp","regresult","install_way","other")
        latest_question_list = list(latest_question_list)
        python2json = {}  # 创建一个字典类型
        python2json["data"] = latest_question_list
        python2json["count"] = len(latest_question_list)
        python2json["msg"] = ""
        python2json["code"] = 0
        data = json.dumps(python2json, ensure_ascii=False)
        print(data)
        return data
    #查询已经安装的私有云
    def GetInstalledPrivate(self,page,limit):
        #先执行mdbg命令查询出所有的私有云
        '''
        result = sendCmd(self.cloudip, self.username, self.pwd,
                         "mdbg -i servermap.moa.kdzl.cn -p 21120 -o exportserver|grep is_private_cloud\(1\)")
        pr_list = result.split("\n")
        for i in range(len(pr_list) - 1):
            # 提取
            # 提取状态
            status = re.findall(r"status\((.+?)\)", pr_list[i])
            status = status[0]
            # 提取srvid
            srvid = re.findall(r"id\((.+?)\)", pr_list[i])
            srvid = srvid[0]
            # 加个判断，先判断数据库里面
            # 提取entryip
            entryip = re.findall(r"pc_entryip\((.+?)\)", pr_list[i])
            entryip = entryip[0]
            if ("pc_entryip()" in pr_list[i]):
                entryip = ""
            # 提取名字
            name = re.findall(r"name\((.+?)\)", pr_list[i])
            name = name[0]
            if ("name()" in pr_list[i]):
                name = ""
            pr = Private.objects.filter(srv_id=srvid).update(status=status,name=name,mdbgrsp=pr_list[i],pc_ip=entryip)
            # 测试账号
        print("保存成功")
        '''
        #再查询数据库里面的数据，返回给列表,先使用切片分页了
        latest_question_list = Private.objects.all().order_by("-srv_id").values("srv_id", "name", "status", "pc_ip",
                                                      "asyncphone",
                                                      "is_lan", "begin_time", "end_time", "num",
                                                      "adminUser", "testAdmin", "testAdminpwd",
                                                      "mdbgrsp", "regresult", "install_way",
                                                      "other")
        #[(int(page) * int(limit)): int(limit)]
        print(int(page)-1)
        print(int(limit))
        begini = (int(page)-1)*int(limit)
        print(begini)
        endi = (int(page)-1)*int(limit)+int(limit)
        latest_question_listall = list(latest_question_list)
        latest_question_list = list(latest_question_list)[begini:endi]
        print(len(latest_question_list))
        python2json = {}  # 创建一个字典类型
        python2json["data"] = latest_question_list
        python2json["count"] = len(latest_question_listall)
        python2json["msg"] = ""
        python2json["code"] = 0
        data = json.dumps(python2json, ensure_ascii=False)
        print(data)
        return data
    def search(self,str):
        if(len(str)==11):
            print("搜索手机号")
            cmd = "get_user_info "+str
            result = sendCmd(self.cloudip, self.username, self.pwd,
                         cmd)
            result = result.replace("\n", "<br>");#这个地方为了适应layyui的弹窗，把换行符换成了<br>
            return result
        elif(len(str) <= 3):
            print("搜索srvid")
            #从数据库查询结果，返回详情
        else:
            print("搜索公司信息")
            cmd = "mdbg -p 21120 -o exportdomain did="+str
            #先查询到servid，在从数据查询结果。可是显示怎么显示？？
            result = sendCmd(self.cloudip, self.username, self.pwd,
                         cmd)
            #提取srvid
            srvid = re.findall(r"srvid\((.+?)\)", result)
            srvid = srvid[0]
            print(srvid)
            #查询详情
            data = self.Getdetail(int(srvid))
            return data
            #获取到

    def Privateroute(self,str):
        print(str)
        jdata = json.loads(str)
        print(jdata)
        if (jdata["action"] == "Regprivate"):
            if (jdata["data"]["installway"] == 1) and (jdata["data"]["privateip"]==""):
                return "没有输入ip，无法创建"
            elif (jdata["data"]["installway"] == 0) and (jdata["data"]["port"]==""):
                jdata["data"]["port"] = "6802"
            if(jdata["data"]["eth"]==""):
                jdata["data"]["eth"] = "eth0"
            if(jdata["data"]["name"]) == "":
                print()
                jdata["data"]["name"] = "moa"+ timezone.now().strftime("%Y-%m-%d")
            result = self.Regprivate(jdata["data"]["deadline"],jdata["data"]["num"],jdata["data"]["sync"],jdata["data"]["installway"],
                                jdata["data"]["privateip"],jdata["data"]["port"],jdata["data"]["eth"],jdata["data"]["name"])
            print(result)
            return result
        if (jdata["action"] == "GetInstalledPrivate"):
            result = self.GetInstalledPrivate(jdata["page"],jdata["limit"])
            return result
        if (jdata["action"] == "search"):
            result = self.search(jdata["keyword"])
            print(result)
            return result
        if (jdata["action"] == "Editprivate"):
            result = self.Editprivate(jdata)
            return result
    if __name__ == "__main__":

       str =  '''
        srvid = 155
        mdbg - p
        24352 - i
        pcdbsync.moa.kdzl.cn - o
        set_limit
        srvid = 155, start = 1517984471000, end = 17296438871000, limit = 10, sn = 4216620015572
        mdbg
        set
        failed
        password = L8z74G645ui72oBB
        '''
        #Regprivate(500,10)
       status = re.findall(r"srvid = (.+?)\n", str)
       print(int(status[0]))
       password =  re.findall(r"password = (.+?)\n", str)
       print(password[0])