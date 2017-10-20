from django.db import models
#import datetime

# Create your models here.
class Privatec(models.Model):
    srv_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200,default="defaultname")
    status = models.CharField()
    pc_ip = models.CharField(max_length=200,default="0.0.0.0")
    is_lan = models.CharField(max_length=100,default="no")
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    usernums = models.IntegerField(default=10)
    activenums = models.IntegerField(default=0)
    adminUser = models.IntegerField()
    testAdmin = models.IntegerField()
    testAdminpwd = models.CharField(max_length=200,default="admin123")
    nothers = models.TextField()
    def __str__(self):
        return self.srv_id


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
