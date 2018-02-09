from django.db import models

import datetime
from django.utils import timezone
class cmds(models.Model):
    cmd = models.CharField(max_length=2000)
    def __str__(self):  # __unicode__ on Python 2
        return self.cmd
class Question(models.Model):
    # qid = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published',default=timezone.now())
    pub_date = models.DateTimeField('date published')
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