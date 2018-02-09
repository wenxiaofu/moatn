from django.db import models

import datetime
from django.utils import timezone
#测试案例表
class TestCase(models.Model):
    name = models.CharField(max_length=200,default="默认名字")
    parent_id = models.IntegerField("父节点", default=0)  # 0代表是跟节点
    case_id = models.AutoField(primary_key=True) #主键递增
    is_parent = models.IntegerField(default=0) #前端0代表，是测试案例，其他代表目录
    needlogin = models.IntegerField(default=1)  # 0代表需要登陆
    srvip = models.CharField(max_length=20,default="200.200.169.212")#服务端ip
    username = models.CharField(max_length=10,default="root")
    rootpwd = models.CharField(max_length=10,default="moatest")
    jsonstr = models.TextField(default="")
    phone = models.CharField(max_length=20,default="")
    phone_pwd = models.CharField(max_length=20,default="12345")
    oprcode = models.CharField(max_length=20,default="")
    servercode = models.CharField(max_length=20,default="")
    verify = models.CharField(max_length=200,default="")
    level = models.IntegerField(default=3)
    case_dec = models.TextField(default="")
#案例执行结果表
class RunResult(models.Model):
    case_id = models.IntegerField(primary_key=True,default=0)
    reqdec = models.TextField(default="")
    resdec = models.TextField(default="")
    ispass = models.IntegerField("ispass",default=1) #1代表没有通过，2代表通过


class Private(models.Model):
    """
       私有云
      """
    # 数据库的模式没有改，需要有个默认值后面改一下
    srv_id = models.IntegerField(primary_key=True,default=0)
    name = models.CharField(max_length=200, default="defaultname")
    status = models.CharField(max_length=200, default="not know")
    pc_ip = models.CharField(max_length=200, default="0.0.0.0")
    asyncphone = models.IntegerField(default=1)#1默认不同步，0为同步
    is_lan = models.CharField(max_length=100, default="no")
    begin_time = models.CharField(max_length=200,default="")
    end_time = models.CharField(max_length=200,default="")
    num = models.IntegerField(default=0)
    adminUser = models.CharField(max_length=100,default="12345678901")
    testAdmin = models.CharField(max_length=100,default="")
    testAdminpwd = models.CharField(max_length=100, default="admin123")
    mdbgrsp = models.TextField(default="")
    regresult = models.TextField(default="")
    install_way = models.TextField(default="")
    other = models.TextField(default="")
    class Meta:
        verbose_name = '私有云'
        verbose_name_plural = '私有云'
    def __str__(self):
        return self.name

class cmds(models.Model):
    cmd = models.CharField(max_length=2000)
    def __str__(self):  # __unicode__ on Python 2
        return self.cmd
class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    #使用timezone.now和使用timezone.now()是有区别的，前者当前时间，后者是应用启动的时间
    pub_date = models.DateTimeField('date published',default=timezone.now)
    def __str__(self):  # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):  # __unicode__ on Python 2
        return self.choice_text