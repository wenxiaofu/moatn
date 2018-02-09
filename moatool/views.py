from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .models import *
from django.core.urlresolvers import reverse
from poll.mfunc.sshclient import verification_ssh
from poll.mfunc.routing import routing
from poll.mfunc.Interfaceroute import Interfacerouting
from poll.mfunc.caseroutec import Caseroutec
import json
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

def sedsshcmd(request):
    return HttpResponse(verification_ssh('200.200.169.212', 'root', 'moatest', 22, 'OrYuWFHeLDBtgX1BitJu', 'mdbg -p 21024 -o exportdomain;ifconfig'))

