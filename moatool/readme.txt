1 python manage.py startapp moatool
2 python manage.py makemigrations
前提条件，需要在mysql里面先创建数据库
主要是连接数据库，创建一些基础管理表格
出现下面这个错误先不用管
MySQL Strict Mode is not set for database connection 'default'
3 增加配置项
moat/settings.py
配置： 'moatprivate.apps.MoatoolConfig'
