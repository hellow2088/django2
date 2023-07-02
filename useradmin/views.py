from functools import wraps

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,ListModelMixin,DestroyModelMixin,UpdateModelMixin

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User,Group

def jsif(request):
    if request.method == 'GET':
        # return render(request,'useradmin/jsif.html')
        return render(request,'useradmin/jstest.html')
    else:
        s = request.POST.get('name1')
        print(s)
        return HttpResponse(s)
# def check_register(func):
#     def inner(request,*args,**kwargs):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         if username == '' or password== '':
#             return HttpResponse('用户名或密码不能空')
#         else:
#             return HttpResponse('ok')
        # for i in username:
        #     if i in ['@','#','$','%','&','*','^']:
        #         return HttpResponse('不能含有特殊字符')
        #     else:
        #         return redirect("/user/login")
    # return inner
from .check_user import checkUser

def register(request):
    if request.method == 'GET':
        return render(request,'useradmin/register.html')
    else:
        data = request.POST
        username = data['username']
        pwd = data['password']
        print(data['username'])
        print(data['password'])
        check_result = checkUser(username,pwd)
        if check_result==None:
            User.objects.create(username=data['username'],nickname=data['nickname'],password=data['password'],
                                gender=data['gender'],email=data['email'])
            return redirect('/user/login.html')
        else:
            return HttpResponse(check_result['msg'])




def logout(request):
    rep = redirect('/user/login/')
    rep.delete_cookie('username')
    request.session.flush()
    return rep

def check_login_cookie(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        #获取cookie
        cookie_value = request.COOKIES.get('username')
        print('check_login_cookie--%s'%cookie_value)
        try:#获取 session
            sessionid = request.session['username']
        except:
            print('没有session')
            sessionid = None
        #如果有session,允许访问url
        if sessionid:
            if cookie_value:
                # 如果存在coookie，继续执行
                return func(request, *args, **kwargs)
            # 如果没有cookie转到登录页面
            else:
                next_url = request.path_info
                return redirect("/user/login".format(next_url))
        else:#如果没有session 则跳转到登录页面
            next_url = request.path_info
            return redirect("/user/login".format(next_url))

    return inner


def check_login_cookie2(request, urls,datas):
    cookie_value = request.COOKIES.get('username')
    print('cookie_value=%s'%cookie_value)
    if cookie_value == "admin":
        # 已经登录，继续执行
        print('*urls=%s'%(urls))
        obj = render(request,urls,datas)
        return obj
    # 没有登录过
    else:
        # ** 即使登录成功也只能跳转到home页面，现在通过在URL中加上next指定跳转的页面
        # 获取当前访问的URL
        next_url = request.path_info
        obj = redirect("/booklist/login".format(next_url))
        return obj


def edituser(request):
    if request.method == 'GET':
        return render(request,'useradmin/edituser.html')
    else:
        pass


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wapper_func(request,*args,**kwargs):
            u = request.COOKIES.get('username')
            uid = User.objects.filter(username=u).values('id')
            if uid:
                uid=uid[0]['id']
            g = Group.objects.filter(user__id=uid).values('gname')
            if g:
                print('111111111111')
                gname = g[0]['gname']
                print('gnamegnamegnamegngnameame',gname)
                print('g=%s,\nrols=%s'%(gname,allowed_roles))

                if gname in allowed_roles:
                    return view_func(request,*args,**kwargs)
                else:
                    return render(request,'useradmin/login.html',{'msg':'没有权限'})
            else:
                return HttpResponse('没有权限<a href="/booklist/showbooks_pagehandle">返回首页</a>')
            return view_func(request,*args,**kwargs)
        return wapper_func
    return decorator


def login(request):
    if request.method == "GET":
        return render(request, 'useradmin/login.html')
    else:
        print('getsession=====',request.session.get('user_id'))
        u = request.POST.get('user')
        p = request.POST.get('password')
        uid = User.objects.filter(username=u).values('id')

        try:
            user = User.objects.get(Q(username=u,password=p))
         
        except:
            return render(request, 'useradmin/login.html', {'msg': '密码或用户名错误'})
            user = None
        #如果验证用户成功，设置cookie和session
        if user:
            print('user=%s,p=%s' % (user.username, user.password))

            obj = redirect('/booklist/showbooks_pagehandle')
            obj.set_cookie('username',u,3600)
            request.session['username'] = u
            return obj

        else:
            # print('123')
            return render(request, 'useradmin/login.html', {'msg': '密码或用户名错误'})


from .forms import loginForm

def login_form(request):
    lf = loginForm()
    print(lf)
    if request.method == 'GET':
        return render(request,'useradmin/login_form.html',{'login_form':lf})

    else:
        return HttpResponse('ok')
