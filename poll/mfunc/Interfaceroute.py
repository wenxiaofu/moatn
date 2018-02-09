import json
from poll.models import Question,Choice,cmds
from poll.mfunc.ctestu import *
#先将所有数据加载到缓存
#http://www.cnblogs.com/xiaojiayu/p/5195298.html
def Interfacerouting(str):
    print(str)
    jdata = json.loads(str)
    if "needlogin" not in jdata["data"]:
        jdata["data"]["needlogin"] = "0"
    if jdata["action"]=="debug" and jdata["data"]["needlogin"] == "0":
        if jdata["data"]["serverip"] == "":
            jdata["data"]["serverip"] = "200.200.169.212"
        #调试，用户名和密码不为空
        if jdata["data"]["username"] == "":
            jdata["data"]["username"] = "root"
        if  jdata["data"]["password"] == "":
            jdata["data"]["password"] = "moatest"
        try:
            print(jdata["data"]["descjson"])
            result = SenYeWu(jdata["data"]["serverip"], jdata["data"]["username"], jdata["data"]["password"],
                             jdata["data"]["phone"], jdata["data"]["phonepwd"], jdata["data"]["oprcode"],
                             jdata["data"]["descjson"])
            #先查询出来对应的数据，查询缓存
            return result
        except KeyError:
            return "ccd"

    elif jdata["action"]=="debug" and jdata["data"]["needlogin"] == "1":
        #不需要登陆，暂时还不用写
        result = SenYeWu(jdata["data"]["serverip"], jdata["data"]["username"], jdata["data"]["password"],
                         jdata["data"]["phone"], jdata["data"]["phonepwd"], jdata["data"]["oprcode"],
                         jdata["data"]["descjson"])
        # 先查询出来对应的数据，查询缓存
        return result
    elif jdata["action"] == "GetSrv":
        if jdata["data"]["serverip"] == "":
            jdata["data"]["serverip"] = "200.200.169.212"
        if jdata["data"]["username"] == "":
            jdata["data"]["username"] = "root"
        if  jdata["data"]["password"] == "":
            jdata["data"]["password"] = "moatest"
        result = GetSrv(jdata["data"]["serverip"], jdata["data"]["username"], jdata["data"]["password"])
        return result
        #这下面解析一下result，返回一个列表过去

    elif jdata["action"] == "GetInterface":
        if jdata["data"]["serverip"] == "":
            jdata["data"]["serverip"] = "200.200.169.212"
        if jdata["data"]["username"] == "":
            jdata["data"]["username"] = "root"
        if  jdata["data"]["password"] == "":
            jdata["data"]["password"] = "moatest"
        result =  GetInterface(jdata["data"]["serverip"], jdata["data"]["username"], jdata["data"]["password"], jdata["data"]["srv"])
        return result
    #路由到获取请求模板的json
    elif jdata["action"] == "GetModel":
        if jdata["data"]["serverip"] == "":
            jdata["data"]["serverip"] = "200.200.169.212"
        if jdata["data"]["username"] == "":
            jdata["data"]["username"] = "root"
        if jdata["data"]["password"] == "":
            jdata["data"]["password"] = "moatest"
        result = GetModel(jdata["data"]["serverip"], jdata["data"]["username"], jdata["data"]["password"], jdata["data"]["interface"])
        return result
