from django.db import models

import datetime
from django.utils import timezone
#测试案例表
class TestCase(models.Model):
    case_id = models.AutoField(primary_key=True)  # 主键递增
    name = models.CharField(max_length=200,default="默认名字")
    parent_id = models.IntegerField("父节点", default=0)  # 0代表是跟节点
    is_parent = models.IntegerField(default=0) #前端0代表，是测试案例，其他代表目录
    needlogin = models.IntegerField(default=1)  # 0代表需要登陆
    srvip = models.CharField(max_length=20,default="200.200.169.212")
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
    private_id = models.AutoField(primary_key=True)  # 主键递增
    srv_id = models.IntegerField("私有云id", default=0)
    name = models.CharField(max_length=200, default="defaultname")
    status = models.CharField(max_length=200, default="not know")
    pc_ip = models.CharField(max_length=200, default="0.0.0.0")
    is_lan = models.CharField(max_length=100, default="no")
    begin_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    usernums = models.IntegerField(default=10)
    activenums = models.IntegerField(default=0)
    adminUser = models.CharField(max_length=200,default="12345678901")
    testAdmin = models.CharField(max_length=200,default="12345678901")
    testAdminpwd = models.CharField(max_length=200, default="admin123")
    nothers = models.TextField()
    class Meta:
        verbose_name = '私有云'
        verbose_name_plural = '私有云'
    def __str__(self):
        return self.name

class cmds(models.Model):
    cmd = models.CharField(max_length=2000)
    def __str__(self):  # __unicode__ on Python 2
        return self.cmd