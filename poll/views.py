from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse
from poll.mfunc.sshclient import verification_ssh
from poll.mfunc.routing import routing
from poll.mfunc.Interfaceroute import Interfacerouting
from poll.mfunc.caseroutec import Caseroutec
import json
from poll.mfunc.private.PrivateRoute import privateR
from django.forms.models import model_to_dict
from django.core import serializers
from django.http import Http404
# Create your views here.

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        # elif isinstance(obj, date):
        #     return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
#实现了接收json，根据json设置路由，返回不同的值
def recjson(request):
    if request.method == 'POST':
        print(request.body.decode('utf-8'))
        received_json_data = json.loads(request.body.decode('utf-8'))
        # received_json_data = json.loads(request.POST)
        print(received_json_data)
        print(received_json_data.keys())
        print(received_json_data["count"])
        print(len(received_json_data["data"]))
        print(received_json_data["data"][1])
        return HttpResponse(request.body.decode('utf-8'))
    else:
        return HttpResponse("参数错误")

    # 业务处理
def pollc(request):
    if request.method == 'POST':
        print(request.body.decode('utf-8'))
        # received_json_data = json.loads(request.POST)
        return HttpResponse(routing(request.body.decode('utf-8')))
    else:
        return HttpResponse("参数错误")


#将查询出来的数据转换成json传给前端
def getcmd(request):
    # python2json = {}
    # python2json["data"]
    # Qs = Questions
    # djson = json.dumps(Qs, ensure_ascii=False)
    # print(djson)
    #http://blog.csdn.net/qq_24861509/article/details/49172945
    # cmd_list = cmds.objects.all()
    # context = {"cmd_list":cmd_list}
    #下面是可以返回想要的结果
    #http://blog.csdn.net/tterminator/article/details/63289400
    latest_question_list = Question.objects.order_by('-pub_date').values("qid","question_text")
    latest_question_list = list(latest_question_list)
    python2json = {}#创建一个字典类型
    python2json["data"] = latest_question_list
    python2json["count"] = len(latest_question_list)
    python2json["msg"] = ""
    python2json["code"] = 0
    data = json.dumps(python2json,ensure_ascii=False)
    print(data)
    # print(latest_question_list)
    # #这里还有一个中文编码的问题没有解决，返回的是16进制字节码，可以自己解析，应该转码的时候就可以解决
    # #使用python的序列化和反序列化
    # data = serializers.serialize("json",latest_question_list)
    # # context = list(latest_question_list)
    #
    # # data = json.dumps(context)
    # print(data)
    return HttpResponse(data)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})
def index_layui(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index_layui.html',context)
def questions(request):
    p1 = request.GET.get('page')
    p2 = request.GET.get('limit')
    print(p1)
    print(p2)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    string1 = '''
    {"code":0,"msg":"","count":1000,"data":[{"id":10000,"username":"user-0","sex":"女","city":"城市-0","sign":"签名-0","experience":255,"logins":24,"wealth":82830700,"classify":"作家","score":57},{"id":10001,"username":"user-1","sex":"男","city":"城市-1","sign":"签名-1","experience":884,"logins":58,"wealth":64928690,"classify":"词人","score":27},{"id":10002,"username":"user-2","sex":"女","city":"城市-2","sign":"签名-2","experience":650,"logins":77,"wealth":6298078,"classify":"酱油","score":31},{"id":10003,"username":"user-3","sex":"女","city":"城市-3","sign":"签名-3","experience":362,"logins":157,"wealth":37117017,"classify":"诗人","score":68},{"id":10004,"username":"user-4","sex":"男","city":"城市-4","sign":"签名-4","experience":807,"logins":51,"wealth":76263262,"classify":"作家","score":6},{"id":10005,"username":"user-5","sex":"女","city":"城市-5","sign":"签名-5","experience":173,"logins":68,"wealth":60344147,"classify":"作家","score":87},{"id":10006,"username":"user-6","sex":"女","city":"城市-6","sign":"签名-6","experience":982,"logins":37,"wealth":57768166,"classify":"作家","score":34},{"id":10007,"username":"user-7","sex":"男","city":"城市-7","sign":"签名-7","experience":727,"logins":150,"wealth":82030578,"classify":"作家","score":28},{"id":10008,"username":"user-8","sex":"男","city":"城市-8","sign":"签名-8","experience":951,"logins":133,"wealth":16503371,"classify":"词人","score":14},{"id":10009,"username":"user-9","sex":"女","city":"城市-9","sign":"签名-9","experience":484,"logins":25,"wealth":86801934,"classify":"词人","score":75},{"id":10010,"username":"user-10","sex":"女","city":"城市-10","sign":"签名-10","experience":1016,"logins":182,"wealth":71294671,"classify":"诗人","score":34},{"id":10011,"username":"user-11","sex":"女","city":"城市-11","sign":"签名-11","experience":492,"logins":107,"wealth":8062783,"classify":"诗人","score":6},{"id":10012,"username":"user-12","sex":"女","city":"城市-12","sign":"签名-12","experience":106,"logins":176,"wealth":42622704,"classify":"词人","score":54},{"id":10013,"username":"user-13","sex":"男","city":"城市-13","sign":"签名-13","experience":1047,"logins":94,"wealth":59508583,"classify":"诗人","score":63},{"id":10014,"username":"user-14","sex":"男","city":"城市-14","sign":"签名-14","experience":873,"logins":116,"wealth":72549912,"classify":"词人","score":8},{"id":10015,"username":"user-15","sex":"女","city":"城市-15","sign":"签名-15","experience":1068,"logins":27,"wealth":52737025,"classify":"作家","score":28},{"id":10016,"username":"user-16","sex":"女","city":"城市-16","sign":"签名-16","experience":862,"logins":168,"wealth":37069775,"classify":"酱油","score":86},{"id":10017,"username":"user-17","sex":"女","city":"城市-17","sign":"签名-17","experience":1060,"logins":187,"wealth":66099525,"classify":"作家","score":69},{"id":10018,"username":"user-18","sex":"女","city":"城市-18","sign":"签名-18","experience":866,"logins":88,"wealth":81722326,"classify":"词人","score":74},{"id":10019,"username":"user-19","sex":"女","city":"城市-19","sign":"签名-19","experience":682,"logins":106,"wealth":68647362,"classify":"词人","score":51},{"id":10020,"username":"user-20","sex":"男","city":"城市-20","sign":"签名-20","experience":770,"logins":24,"wealth":92420248,"classify":"诗人","score":87},{"id":10021,"username":"user-21","sex":"男","city":"城市-21","sign":"签名-21","experience":184,"logins":131,"wealth":71566045,"classify":"词人","score":99},{"id":10022,"username":"user-22","sex":"男","city":"城市-22","sign":"签名-22","experience":739,"logins":152,"wealth":60907929,"classify":"作家","score":18},{"id":10023,"username":"user-23","sex":"女","city":"城市-23","sign":"签名-23","experience":127,"logins":82,"wealth":14765943,"classify":"作家","score":30},{"id":10024,"username":"user-24","sex":"女","city":"城市-24","sign":"签名-24","experience":212,"logins":133,"wealth":59011052,"classify":"词人","score":76},{"id":10025,"username":"user-25","sex":"女","city":"城市-25","sign":"签名-25","experience":938,"logins":182,"wealth":91183097,"classify":"作家","score":69},{"id":10026,"username":"user-26","sex":"男","city":"城市-26","sign":"签名-26","experience":978,"logins":7,"wealth":48008413,"classify":"作家","score":65},{"id":10027,"username":"user-27","sex":"女","city":"城市-27","sign":"签名-27","experience":371,"logins":44,"wealth":64419691,"classify":"诗人","score":60},{"id":10028,"username":"user-28","sex":"女","city":"城市-28","sign":"签名-28","experience":977,"logins":21,"wealth":75935022,"classify":"作家","score":37},{"id":10029,"username":"user-29","sex":"男","city":"城市-29","sign":"签名-29","experience":647,"logins":107,"wealth":97450636,"classify":"酱油","score":27}]}
    '''
    return HttpResponse(string1)
def lay(request):
     #
     qss = Question(question_text="testweew")
     print(qss)
     return render(request, 'poll/lay.html')

def testu(request):
    if request.method == 'POST':
        print(request.body.decode('utf-8'))
        # received_json_data = json.loads(request.POST)
        return HttpResponse(Interfacerouting(request.body.decode('utf-8')))
    else:
        return HttpResponse("参数错误")

def caseu(request):
    if request.method == 'POST':
        print(request.body.decode('utf-8'))
        # received_json_data = json.loads(request.POST)
        return HttpResponse(Caseroutec(request.body.decode('utf-8')))
    else:
        return HttpResponse("参数错误")
def private(request):
    if request.method == 'POST':
        print(request.body.decode('utf-8'))
        # received_json_data = json.loads(request.POST)
        print("-----------------")
        pv = privateR()
        return HttpResponse(privateR.Privateroute(pv,request.body.decode('utf-8')))
    elif request.method == 'GET':
        python2json = {}  # 创建一个字典类型
        python2json["action"] = request.GET.get("action")
        python2json["page"] = request.GET.get("page")
        python2json["limit"] = request.GET.get("limit")
        python2json["code"] = 0
        python2json["keyword"] = request.GET.get("keyword")
        data = json.dumps(python2json, ensure_ascii=False)
        pv = privateR()
        if request.GET.get("action") == "detail":
            #查询数据库
            private_list = Private.objects.filter(srv_id=request.GET.get("srvid"))
            context = {'private_list': private_list}
            return render(request, 'privatedetail.html', context)
        return HttpResponse(privateR.Privateroute(pv, data))
    else:
        return HttpResponse("参数错误")

def sedsshcmd(request):
    return HttpResponse(verification_ssh('200.200.169.212', 'root', 'moatest', 22, 'OrYuWFHeLDBtgX1BitJu', 'mdbg -p 21024 -o exportdomain;ifconfig'))

def layuitable(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/layuitable.html', context)

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:results', args=(p.id,)))