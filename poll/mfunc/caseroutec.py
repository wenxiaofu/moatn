import json
from poll.models import Question,TestCase,RunResult
from django.db.models import F
from poll.mfunc.ctestu import *
#先将所有数据加载到缓存
#http://www.cnblogs.com/xiaojiayu/p/5195298.html
def Caseroutec(str):
    print(str)
    jdata = json.loads(str)
    #编辑
    if jdata["action"]=="find":
        try:
            #怎么把查询出来的数据转换为json,这里只查询id和name，查询单个才查询详情
            #查询目录和测试案例
            if jdata["model"] == "all":
                #User.objects.annotate(nick=F('coreuserwxprofile__nickname')).values('id', 'nick') 下面使用别名
                latest_question_list = TestCase.objects.annotate(id=F('case_id'),pId=F('parent_id'),isParent=F('is_parent')).values("id", "name","pId","isParent") #这样才可以转换成json，不加values，返回的是一个set类形
                #先转换成数组
                latest_question_list = list(latest_question_list)
                python2json = {}  # 创建一个字典类型
                python2json["data"] = latest_question_list
                python2json["count"] = len(latest_question_list)
                python2json["msg"] = ""
                python2json["code"] = 0
                data = json.dumps(python2json, ensure_ascii=False)
                return data
            #查询目录
            if jdata["model"] == "context":
                #增加筛选条件
                latest_question_list = TestCase.objects.filter(is_parent=1).values("case_id", "name")  # 这样才可以转换成json，使用objectall不可以
                latest_question_list = list(latest_question_list)
                python2json = {}  # 创建一个字典类型
                python2json["data"] = latest_question_list
                python2json["count"] = len(latest_question_list)
                python2json["msg"] = ""
                python2json["code"] = 0
                data = json.dumps(python2json, ensure_ascii=False)
                print(data)
                return data
        except KeyError:
            return "参数错误，没有选择某一个类型"
    elif jdata["action"] == "create":
        if jdata["model"] == "context":
            try:
                ts = TestCase()
                ts.parent_id = jdata["data"]["parent_id"]
                ts.name = jdata["data"]["case_name"]
                ts.is_parent = 1
                ts.save()
                return ts.case_id
            except KeyError:
                return "参数错误"
        elif jdata["model"] == "case":
            try:
                ts = TestCase()
                ts.parent_id = jdata["data"]["contextchosed"]
                ts.case_dec = jdata["data"]
                ts.name = jdata["data"]["case_name"]
                ts.verify = jdata["data"]["verify"]
                ts.username = jdata["data"]["username"]
                ts.rootpwd = jdata["data"]["password"]
                ts.phone = jdata["data"]["phone"]
                ts.phone_pwd = jdata["data"]["phonepwd"]
                ts.servercode = jdata["data"]["srvcode"]
                ts.oprcode = jdata["data"]["oprcode"]
                ts.jsonstr = jdata["data"]["descjson"]
                ts.needlogin = jdata["data"]["needlogin"]
                ts.srvip = jdata["data"]["serverip"]
                ts.is_parent = 0
                ts.save()
                return ts.case_id
            except KeyError:
                return "参数错误"
    #获取案例详情
    elif jdata["action"] == "getdetail":
        try:
            # 怎么把查询出来的数据转换为json,这里只查询id和name，查询单个才查询详情
                # User.objects.annotate(nick=F('coreuserwxprofile__nickname')).values('id', 'nick') 下面使用别名
                latest_question_list = TestCase.objects.filter(case_id=jdata["id"]).annotate(id=F('case_id'), pId=F('parent_id')).values("id",
                "name","pId","case_dec","needlogin","srvip","username","rootpwd","jsonstr","phone","phone_pwd","oprcode","servercode"
                ,"verify","level","is_parent")  # 这样才可以转换成json，不加values，返回的是一个set类形
                # 先转换成数组
                tsresult = RunResult.objects.filter(case_id=jdata["id"])
                latest_question_list = list(latest_question_list)
                python2json = {}  # 创建一个字典类型
                python2json["data"] = latest_question_list
                python2json["count"] = len(latest_question_list)
                python2json["msg"] = ""
                python2json["code"] = 0
                if len(tsresult) == 1:#防止越界
                    python2json["reqdec"] = tsresult[0].resdec
                data = json.dumps(python2json, ensure_ascii=False)
                print(data)
                return data
        except KeyError:
            return "参数错误，没有选择某一个类型"
    elif jdata["action"] == "edit":
        try:
            # 怎么把查询出来的数据转换为json,这里只查询id和name，查询单个才查询详情
                # User.objects.annotate(nick=F('coreuserwxprofile__nickname')).values('id', 'nick') 下面使用别名
                ts = TestCase.objects.filter(case_id=jdata["data"]["case_id"]).update(name=jdata["data"]["name"],srvip = jdata["data"]["serverip"]
                    ,username = jdata["data"]["username"],rootpwd = jdata["data"]["password"],phone = jdata["data"]["phone"],jsonstr = jdata["data"]["descjson"]
                    ,verify = jdata["data"]["verify"])
                return "保存成功"
        except KeyError as e:
            return e
    elif jdata["action"] == "run":
        rel = {}
        try:
            print(jdata["id"])

            ts = TestCase.objects.filter(case_id=jdata["id"])
            print(ts)
            #先查询出对应的测试案例，取出对应的数据
            result = SenYeWu(ts[0].srvip, ts[0].username, ts[0].rootpwd,
                             ts[0].phone, ts[0].phone_pwd, ts[0].oprcode,
                             ts[0].jsonstr)
            print(ts[0].srvip)
            if ts[0].needlogin == 0:
                try:
                    result = SenYeWu(ts[0].srvip, ts[0].username, ts[0].rootpwd,
                                     ts[0].phone,ts[0].phone_pwd, ts[0].oprcode,
                                     ts[0].jsonstr)

                    # 先查询出来对应的数据，查询缓存
                    tsresult = RunResult()
                    tsresult.case_id = ts[0].case_id
                    tsresult.ispass = 2 #暂时先这样
                    tsresult.resdec = result
                    tsresult.reqdec = ts[0].jsonstr
                    tsresult.save()
                    if ts[0].verify == "":
                        rel["rel"] = "案例通过"
                        rel["i"] = jdata["i"]
                        rel = json.dumps(rel, ensure_ascii=False)
                        return rel
                    else:
                        #校验verify是否在响应中,需要兼容verrify为空的时候

                        listv = ts[0].verify.split(';')
                        for a in listv:
                            if a in result:
                                rel["rel"] = "案例通过"
                                rel["i"] = jdata["i"]
                                rel = json.dumps(rel, ensure_ascii=False)
                                print(rel)
                                return rel
                            else:
                                rel["rel"] = "案例失败"
                                rel["i"] = jdata["i"]
                                rel = json.dumps(rel, ensure_ascii=False)
                                return rel #超时时间，如果超过4秒就会有问题
                except KeyError:
                    return "ccd"

            print()

        except KeyError:
            return "参数错误"
    elif jdata["action"] == "del":
        try:
            ts = TestCase.objects.filter(case_id=jdata["id"])
            #查询当前目录下是否有子案例和目录
            child = TestCase.objects.filter(parent_id=jdata["id"])
            if len(child) == 0:
               result = ts.delete()
               return result[0] #这里会返回1
            else:
                return 0;#代表没有删除
            #先查询出对应的测试案例，取出对应的数据
        except KeyError:
            return "参数错误,删除失败"


    else:
        return "no ready now"
