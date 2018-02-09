import json
from poll.models import Question,Choice,cmds,Private
#先将所有数据加载到缓存
#http://www.cnblogs.com/xiaojiayu/p/5195298.html
def routing(str):
    print(str)
    jdata = json.loads(str)
    if jdata["model"]=="poll":
        #编辑
        if jdata["action"]=="edit":
            try:
                #先查询出来对应的数据，查询缓存
                Qs = Question(qid=jdata["data"]["qid"])
                Qs.question_text = jdata["data"]["question_text"]
                Qs.save()
                return "修改成功"
            except KeyError:
                return "参数错误"
        elif jdata["action"] == "create":
            try:
                Qs = Question()
                Qs.question_text = jdata["data"]["question_text"]
                Qs.save()
                return "保存成功"
            except KeyError:
                return "参数错误"
        elif jdata["action"] == "del":
            Qs = Question(qid=jdata["data"]["qid"])
            Qs.delete()
            return "删除成功"
        else:
            return "参数错误"
    elif jdata["model"]=="private":
        #编辑
        if jdata["action"]=="edit":
            try:
                #先查询出来对应的数据，查询缓存
                Qs = Question(qid=jdata["data"]["pid"])
                Qs.question_text = jdata["data"]["question_text"]
                Qs.save()
                return "修改成功"
            except KeyError:
                return "参数错误"
        elif jdata["action"] == "create":
            try:
                Ps = Private()
                Ps.srv_id = jdata["data"]["srv_id"]
                Ps.name = jdata["data"]["name"]
                Ps.pc_ip = jdata["data"]["pc_ip"]
                Ps.nothers = jdata["data"]["nothers"]
                Ps.save()
                return "保存成功"
            except KeyError:
                return "参数错误"
        elif jdata["action"] == "del":
            Qs = Question(qid=jdata["data"]["qid"])
            Qs.delete()
            return "删除成功"
        else:
            return "参数错误"

    else:
        return "no ready now"
