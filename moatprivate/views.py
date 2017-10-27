from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Privatec
def AddPrivatec():
    print("add")
def ShowDetail(request,srvid):
    a_list = Privatec.objects.filter(srv_id=srvid)
    context = {"srvid":srvid,"Privatec":a_list}
    return render(request,'moatprivate/detail.html',context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")