from functools import wraps
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
import json
import pymysql
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .Myserializer import BookSerializer
from .models import *
from django.contrib.auth.decorators import login_required
from useradmin.views import check_login_cookie
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, \
    RetrieveModelMixin
from rest_framework.generics import ListCreateAPIView
from django.views import View
# from . import serializer
from .serializer import OrganizationSerializer, HeroSerializer


def vuetest(request):
    content = {'name':'Mike'}
    return render(request,'bookdrt/update_book.html',content)


class BookView(View):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误'}, status=400)

        bs = BookSerializer(book)
        return JsonResponse(bs.data,safe=False)

    def put(self, request, pk):
        data = request.body.decode()
        data_dict = json.loads(data)
        try:
            book = Book.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误信息'}, status=400)

        book.title = data_dict.get('title')
        book.writer = data_dict.get('writer')
        book.press = data_dict.get('press')
        book.date = data_dict.get('date')

        book.save()
        bs = BookSerializer(book)
        return JsonResponse(bs.data,safe=False)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误'}, status=400)
        book.is_delete = True
        book.save()
        return JsonResponse({})


class BooksView(APIView):
    def get(self, request):
        print(request)
        books = Book.objects.all()
        print(books)
        bs = BookSerializer(books,many=True)
        return JsonResponse(bs.data,safe=False)

    def post(self, request):
        data = request.body.decode()
        print(data)
        data_dict = json.loads(data)
        bs = BookSerializer(data=data_dict)
        bs.is_valid()
        bs.save()
        return JsonResponse(bs.data)

class OrganizationView(View):
    def get(self,request):
        org = Organization.objects.all()
        orgs = OrganizationSerializer(org,many=True)
        return JsonResponse(orgs.data,safe=False)

    def post(self,request):
        org = request.body.decode()
        org = json.loads(org)
        print(org)
        orgname = org.get('orgname')
        district = org.get('district')
        scale = org.get('scale')
        established_time = org.get('established_time')
        if orgname is None or orgname=='':
            return JsonResponse({'error': '错误信息'}, status=400)
        new_org = Organization.objects.create(orgname=orgname,district=district,scale=scale,established_time=established_time)
        new_org.save()
        orgs = OrganizationSerializer(new_org)
        return JsonResponse(orgs.data,safe=False)



class HeroView(View):
    def get(self,request):
        hero = Hero.objects.all()

        heros = HeroSerializer(hero,many=True)

        return JsonResponse(heros.data,safe=False)
    def post(self,request):
        hero = request.body.decode()
        hero = json.loads(hero)
        print(hero)
        name = hero.get('name')
        skill = hero.get('skill')
        book_id = hero.get('book')
        org_id = hero.get('org')
        if name is None or name=='':
            return JsonResponse({'error': '错误信息'}, status=400)
        new_hero = Hero.objects.create(name=name,skill=skill,book_id=book_id,org_id=org_id)
        new_hero.save()
        new_heros = HeroSerializer(new_hero)
        return JsonResponse(new_heros.data,safe=False)


class HeroListView(ListView):
    model = Hero
    template_name = 'booklist/writer_list.html'
    context_object_name = 'writer_list'
    queryset = Hero.objects.all()


from useradmin.views import allowed_users


@check_login_cookie
@allowed_users(allowed_roles=['emp'])
def showhero(request):
    results = Hero.objects.all()
    # for i in results:
    #     print(i,i.skill,i.book,i.org.orgname)
    return render(request, 'booklist/showhero.html', {'results': results})


def delhero(request):
    nid = request.GET.get('nid')
    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='test',
    #                        charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("delete from booklist_hero where id=%s", [nid, ])
    # conn.commit()
    # cursor.close()
    # conn.close()
    Hero.objects.get(id=nid).delete()
    return redirect('/booklist/showhero')


def addhero(request):
    if request.method == 'GET':
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='bookstore',
                               charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sqlbook = """select * from booklist_book;"""
        cursor.execute(sqlbook)
        book = cursor.fetchall()
        sqlorg = """select * from booklist_organization;"""
        cursor.execute(sqlorg)

        org = cursor.fetchall()

        content = {'book': book, 'org': org}
        cursor.close()
        conn.close()
        return render(request, 'booklist/addhero.html', content)

    else:
        # print(request.POST)
        hname = request.POST.get('hname')
        skill = request.POST.get('skill')
        bookid = request.POST.get('bookid')
        orgid = request.POST.get('orgid')
        print(len(hname))
        if len(hname) > 0:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='bookstore',
                                   charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

            sql = """insert into booklist_hero(hname, skill, org_id, book_id) values(%s,%s,%s,%s)"""
            l = [hname, skill, orgid, bookid]
            # print(l)
            cursor.execute(sql, l)
            conn.commit()

            cursor.close()
            conn.close()
            # print(request.POST.get('title'))
            return redirect('/booklist/showhero/')

        else:
            return render(request, 'booklist/addhero.html', {'msg': '姓名不能为空'})


def edithero(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='bookstore',
                               charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(
            "select bh.id,bh.hname,bh.book_id,bh.org_id,bb.title,bo.orgname,bh.skill from booklist_book bb,booklist_hero bh,booklist_organization bo where bb.id = bh.book_id and bh.org_id=bo.id and bh.id=%s",
            [nid, ])
        hero = cursor.fetchone()
        cursor.execute("select * from booklist_book")
        book = cursor.fetchall()
        cursor.execute("select * from booklist_organization")
        org = cursor.fetchall()
        content = {'hero': hero, 'book': book, 'org': org}

        cursor.close()
        conn.close()
        return render(request, 'booklist/edithero.html', content)

    else:
        nid = request.GET.get('nid')
        hname = request.POST.get('hname')
        bookid = request.POST.get('bookid')
        skill = request.POST.get('skill')
        orgid = request.POST.get('orgid')
        # print(len(hname))
        if len(hname) > 0:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='test',
                                   charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute("update booklist_hero set hname = %s,skill = %s,org_id = %s,book_id = %s where id=%s",
                           [hname, skill, orgid, bookid, nid])
            conn.commit()
            cursor.close()
            conn.close()

            return redirect('/booklist/showhero/')

        else:
            return render(request, 'booklist/edithero.html', {'msg': 'name and skill cant be null'})


class BooklistView(ListView):
    model = Book
    template_name = 'booklist/lvbooks.html'
    context_object_name = 'booklist'
    queryset = Book.objects.all()
    # def getBooks(self,**args):
    #     books = Book.objects.all()
    #     return books


# def HeroInfo(request, hid):
#     h = Hero.objects.get(pk=hid)
#     context = {'h': h}
#     print(h)
#     return render(request, 'booklist/heroinfo.html', context)


def addbook(request):
    if request.method == 'GET':

        return render(request, 'booklist/addbook.html')
    else:
        # print(request.POST)
        title = request.POST.get('title')
        press = request.POST.get('press')
        date = request.POST.get('date')
        binfo = request.POST
        print('binfo=%s' % binfo)
        if len(title) > 0:
            Book.objects.create(title=title, press=press, date=date)

            return redirect('/booklist/showbooks_pagehandle/?page=1')
        else:
            return render(request, 'booklist/addbook.html', {'msg': '书名不能为空'})


def windowaddbook(request):
    print(123)
    title = request.POST.get('title')
    # writer = request.POST.get('writer')
    press = request.POST.get('press')
    date = request.POST.get('date')

    if len(title) > 0:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='bookstore',
                               charset='utf8')
        cursor = conn.cursor()

        sql = """insert into booklist_book(title, press, date) values(%s,%s,%s)"""
        l = (title, press, date)
        print(l)
        cursor.execute(sql, l)
        conn.commit()

        cursor.close()
        conn.close()
        return HttpResponse('OK')
    else:
        return HttpResponse('书籍名称不能为空')


def editbook(request, nid):
    if request.method == 'GET':
        print(nid)
        book = Book.objects.get(id=nid)
        return render(request, 'booklist/editbook.html', {'book': book})

    else:
        nid = request.POST.get('id')
        title = request.POST.get('title')
        press = request.POST.get('press')
        date = request.POST.get('date')

        Book.objects.filter(id=nid).update(title=title, press=press, date=date)
        # Book.objects.filter(id=1).update(title='Book1', press='press1', date='2001-01-02')

        return redirect('/booklist/showbooks2/')


def modelEditbook(request):
    ret = {'status': True, 'msg': None}

    try:
        nid = request.POST.get('nid')
        title = request.POST.get('title')
        # writer = request.POST.get('writer')
        press = request.POST.get('press')
        date = request.POST.get('date')
        # print([title, writer, press, date, nid])
        if len(title) > 0:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='bookstore',
                                   charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute("update booklist_book set title = %s,press = %s,date = %s where id=%s",
                           [title, press, date, nid])

            conn.commit()
            cursor.close()
            conn.close()
        else:
            ret['status'] = False
            ret['msg'] = '书名不能为空'

    except Exception as e:
        ret['status'] = False
        ret['msg'] = '更新失败'

    return HttpResponse(json.dumps(ret))


def delbook(request):
    nid = request.GET.get('nid')
    Book.objects.get(id=nid).delete()
    return redirect('/booklist/showbooks')


def test(request):
    return render(request, 'booklist/test.html')


def getdata(request):
    print(123)
    data = request.POST.get('data')
    print(data)
    return HttpResponse('ok')


def windowaddbook2(request):
    title = request.POST.get('title')
    # writer = request.POST.get('writer')
    press = request.POST.get('press')
    date = request.POST.get('date')

    if len(title) > 0:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='bookstore',
                               charset='utf8')
        cursor = conn.cursor()

        sql = """insert into booklist_book(title, press, date) values(%s,%s,%s)"""
        l = (title, press, date)
        print(l)
        cursor.execute(sql, l)
        conn.commit()

        cursor.close()
        conn.close()
        return HttpResponse('OK')
    else:
        return HttpResponse('书籍名称不能为空')

from django.views import View


class Login(View):

    def dispatch(self, request, *args, **kwargs):
        obj = super(Login, self).dispatch(request, *args, **kwargs)
        print('from dispatch')
        return obj

    def get(self, request):
        return render(request, 'booklist/login.html')

    def post(self, request):
        username = request.POST.get('user')
        pwd = request.POST.get('password')

        if username == 'admin' and pwd == '123':
            return redirect('/booklist/showbooks')
        else:
            return HttpResponse('密用户名或密码错误')


def getmsg(request):
    msg = request.POST
    l = ['a', 'b', 'c', 'd', 'e', 'f']
    return render(request, 'booklist/getmsg.html', {'msg': msg, 'l': l})
