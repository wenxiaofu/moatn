from django.db import models
from django.utils import timezone
#import datetime

# Create your models here.
class Privatec(models.Model):
    """
     私有云
    """
    #数据库的模式没有改，需要有个默认值后面改一下
    srv_id = models.IntegerField("私有云id",default=0)
    name = models.CharField(max_length=200,default="defaultname")
    status = models.CharField(max_length=200,default="not know")
    pc_ip = models.CharField(max_length=200,default="0.0.0.0")
    is_lan = models.CharField(max_length=100,default="no")
    begin_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    usernums = models.IntegerField(default=10)
    activenums = models.IntegerField(default=0)
    adminUser = models.IntegerField(default=123456)
    testAdmin = models.IntegerField(default=123456)
    testAdminpwd = models.CharField(max_length=200,default="admin123")
    nothers = models.TextField(default="no notice")
    class Meta:
        verbose_name = '私有云'
        verbose_name_plural = '私有云'
    def __str__(self):
        return self.name
    def make_published(modeladmin, request, queryset):
        queryset.update(status='p')
    make_published.short_description = "Mark selected stories as published"
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):  # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):  # __unicode__ on Python 2
            return self.choice_text

