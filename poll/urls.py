from django.conf.urls import url

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
    url(r'^lay/$',views.lay,name='lay')
]