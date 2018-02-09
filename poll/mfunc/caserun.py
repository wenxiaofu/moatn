from poll.mfunc.caseroutec import Caseroutec
from poll.models import Question,TestCase
import json
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poll.settings")# project_name 项目名称
django.setup()
def Caserun(id):
    ts = TestCase.objects.filter(case_id=4)
    # 解析案例内容
    jsonstr = ts[0].case_dec
    # 转换成json
    jsonstr = json.dumps(ts.case_dec)

    print()