from django.conf.urls import url
app_name='poll'
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^index_layui/',views.index_layui,name='index_layui'),
    url(r'^layuitable/',views.layuitable,name='layuitable'),
    url(r'^questions/$',views.questions,name='questions'),#后面增加/$是为了支持添加参数
    url(r'^lay/$',views.lay,name='lay'),
    url(r'^sedsshcmd/$',views.sedsshcmd,name='sedsshcmd'),
    url(r'^getcmds/$',views.getcmd,name='getcmd'),
    url(r'^recjson/$',views.recjson,name='recjson'),
    url(r'pollc/$',views.pollc,name='pollc'),
    url(r'^testu/$',views.testu,name='testu'),#接口调试
    url(r'^caseu/$',views.caseu,name='caseu'),#测试案例
    url(r'^private/$',views.private,name='private'),#测试案例
]