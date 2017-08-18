python manage.py runserver

django-admin startapp TestModel




$ python manage.py migrate   # 创建表结构

$ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate TestModel   # 创建表结构



然后在浏览器中访问 http://127.0.0.1:8000/admin/


# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@runoob.com
Password:
Password (again):
Superuser created successfully.
[root@solar HelloWorld]#

test增加 test3.py
python manage.py  test TestModel.test3.MyTest.test_case
