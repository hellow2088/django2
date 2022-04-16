from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import registerForm, loginForm, cgpwdForm
import json
from django.http import JsonResponse

from mytest.utils.getValidimg import getValidCode

def get_validCode_img(request):
    dimg = getValidCode(request)

    return HttpResponse(dimg)


def index(request):
    return render(request, 'mytest/index.html')


def register(request):
    rgform = registerForm()
    if request.method == 'GET':
        return render(request, 'mytest/register.html', {'rgform': rgform})
    # User.objects.create(username='runboo',password='123')

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create(username=username, password=password)

        return HttpResponse(username)


from django.contrib import auth


def mylogin(request):
    # login(request,user)
    loginform = loginForm()
    # u = auth.authenticate(username='admin', password='admin123')
    # print(u)
    if request.method == 'GET':
        return render(request, 'mytest/login.html', {'loginform': loginform})
    else:
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        validCode = request.POST.get('validCode')
        print(username, password)
        response = {'user': None, 'msg': None}
        validCode_string = request.session['validCode_string']
        if validCode.upper() == validCode_string.upper():
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                response['user'] = username
                response['msg'] = '用户验证成功'
            else:
                response['msg'] = 'username or password wrong.'

        else:
            response['msg'] = 'valid wrong'

        return JsonResponse(response)


def cgpwd(request):
    cgform = cgpwdForm()
    if request.method == 'GET':
        return render(request, 'mytest/cgpwd.html', {'cgform': cgform})

    else:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        print(user)
        user.set_password(password)
        user.save()
        print(user.set_password(password))

        return HttpResponse('ok')

    # valid_num = request.POST.get('valid_num')


#   	keep_str = request.session.get('keep_str')
# print(valid_num)
# return HttpResponse('ok')


def ajtest(request):
    if request.method == 'GET':
        return render(request, 'mytest/ajax_test.html')

    else:
        ret = {'status': True, 'msg': None}
        pdata = request.POST
        ret['msg'] = 'good'
        print(pdata)
        print(ret)

        return HttpResponse(json.dumps(ret))


def repajax(request):
    if request.method == 'GET':
        return HttpResponse('hello')
