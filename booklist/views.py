from functools import wraps

from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
import json
import pymysql
from .utils import sqlhandle
from .utils.pagehandle import PageInfo
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required

from useradmin.views import check_login_cookie

import logging
# 设置打印日志的级别，level级别以上的日志会打印出
# level=logging.DEBUG 、INFO 、WARNING、ERROR、CRITICAL
logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                    level=logging.DEBUG)


def vuetest(request):
    logging.debug(request)
    content = {'name':'Mike'}
    return render(request,'booklist/vuetest.html',content)



class WriterListView(ListView):
    model = Writer
    template_name= 'booklist/writer_list.html'
    context_object_name ='writer_list'
    queryset = Writer.objects.all()


def addwriter(request):
    if request.method == 'GET':
        btitle = sqlhandle.search('select * from booklist_book')
        return render(request, 'booklist/addwriter.html', {'btitle': btitle})
    else:
        wname = request.POST.get('wname')
        wage = request.POST.get('wage')
        bid = request.POST.getlist('bid')
        # print(wname,wage)
        wid = sqlhandle.update('insert into booklist_writer(wname,wage) values(%s,%s)', [wname, wage])

        for bid in bid:
            sqlhandle.update('insert into booklist_book_writer(bid,wid) values(%s,%s)', [bid, wid])
        return redirect('/booklist/showwriter/')


def editwriter(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        writer = sqlhandle.getone('select * from booklist_writer where id=%s', [nid, ])
        bookid = sqlhandle.search(
            'select bid from booklist_book_writer where wid=%s', [nid, ])
        bookidlist = []
        for bid in bookid:
            bookidlist.append(bid['bid'])
        book = sqlhandle.search('select * from booklist_book')
        # print(bookidlist)
        return render(request, 'booklist/editwriter.html', {'writer': writer, 'book': book, 'bookidlist': bookidlist})

    else:
        nid = request.POST.get('nid')
        wname = request.POST.get('wname')
        wage = request.POST.get('wage')
        bookid = request.POST.getlist('bid')
        # print(bookid)
        sqlhandle.update('update booklist_writer set wname =%s,wage=%s where id=%s ', [wname, wage, nid])

        bid = sqlhandle.search('select bid from booklist_book_writer where wid=%s', [nid, ])
        bidlist = []
        for bid in bid:
            bidlist.append(bid['bid'])

        sqlhandle.update('delete from booklist_book_writer where wid=%s', [nid, ])

        for bookid in bookid:
            sqlhandle.update('insert into booklist_book_writer(bid,wid) values (%s,%s)', [bookid, nid])


        return redirect('/booklist/showwriter/')


def getwriter(request):
    import time
    time.sleep(0.5)
    writer = sqlhandle.search('select * from booklist_writer')
    return HttpResponse(json.dumps(writer))


def modal_addwriter(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    bid = request.POST.getlist('wid')
    wid = sqlhandle.update('insert into booklist_writer(wname,wage) values(%s,%s)', [name, age])
    print(wid)
    for bid in bid:
        sqlhandle.update('insert into booklist_book_writer(bid,wid) values(%s,%s)', [bid, wid])

    return HttpResponse('ok')

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
    model  = Book
    template_name = 'booklist/lvbooks.html'
    context_object_name  = 'booklist'
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

@login_required()
def showbooks(request):
    results = Book.objects.all()
    # print(results)
    all_count = Book.objects.all().count()
    current_page = request.GET.get('page')
    page_info = PageInfo(current_page,all_count,10,'/booklist/showbooks/')
    booklist = Book.objects.all()[page_info.start():page_info.end()]
    # print(booklist)

    return render(request, 'booklist/showbooks.html', {'book': booklist,'page_info':page_info})

def editbook(request,nid):
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


def bookhero(request):
    book = sqlhandle.search(
        'select bb.id,bb.title,bh.hname from booklist_book bb left join booklist_hero bh on bb.id=bh.book_id')

    # print(book[0])
    results = {}
    for b in book:
        bid = b['id']
        # print(bid)
        if bid in results:
            results[bid]['hname'].append(b['hname'])
        else:
            results[bid] = {'id': b['id'], 'title': b['title'], 'hname': [b['hname'], ]}

    print(results)
    return render(request, 'booklist/bookhero.html', {'results': results.values()})
    # return HttpResponse('ok')


def window(request):
    return render(request, 'booklist/window.html')


def showbooks2(request):
    # ck = request.COOKIES.get('cookie')
    # ck = request.get_signed_cookie('cookie', salt='gggggg')

    # if not ck:
    #     return redirect('/booklist/login/')
    book_counts = Book.objects.all().count()
    current_page = request.GET.get('page')#?page=3
    if current_page:
        if int(current_page)<=0:
            current_page = 1
    pageinfo = PageInfo(current_page,book_counts,2,'/booklist/showbooks2/')
    results = Book.objects.all()[pageinfo.start():pageinfo.end()]#当前页展示书籍，从第几本开始，到第几本结束
    #返回的是当前页的数据数量
    return render(request, 'booklist/showbooks2.html', {'book': results,'pageinfo':pageinfo,'current_page':pageinfo.current_page})

from .utils.page_handle import pageino,current_page_handle
import math

@check_login_cookie
def showbooks_pagehandle(request):
    # if request.method == 'GET':

    keyword = request.GET.get('q')
    kd=''
    kwd=''
    if keyword:
        results = Book.objects.filter(title__contains=keyword)
        book_counts = Book.objects.filter(title__contains=keyword).count()
        kd = 'q='+keyword+'&'
        kwd = keyword

    else:
        book_counts = Book.objects.all().count()
        results = Book.objects.all()


    current_page = request.GET.get('page')#?page=3
    per_page_num = 3
    showpages = 11
    total_pages = math.ceil(book_counts / per_page_num)
    current_page = current_page_handle(book_counts,per_page_num,current_page)
    # print('current_page=%s'%current_page)
    p = pageino(book_counts,per_page_num,current_page,showpages)
    showpages = p.showpages()
    sn = p.current_data()

    next_prev = p.next_prev()

    showpages = [x for x in range(1,showpages+1)]
    results = results[sn[0]:sn[1]]#当前页展示书籍，从第几本开始，到第几本结束
    print(results)
    context = {'book': results,'showpages':showpages,'current_page':current_page,
               'next_prev':next_prev,'total_pages':total_pages,'kd':kd,'kwd':kwd
               }
    #返回的是当前页的数据数量
    return render(request, 'booklist/showbooks_pagehandle.html', context)

def search(request):
    # if request.method == "POST":
    keyword = request.GET.get('q')
    print(keyword)
    results = Book.objects.filter(title__contains=keyword)
    book_counts = Book.objects.filter(title__contains=keyword).count()
    print(results)

   

    current_page = request.GET.get('page')#?page=3
    per_page_num = 3
    showpages = 11
    total_pages = math.ceil(book_counts / per_page_num)
    current_page = current_page_handle(book_counts,per_page_num,current_page)
    # print('current_page=%s'%current_page)
    p = pageino(book_counts,per_page_num,current_page,showpages)
    showpages = p.showpages()
    sn = p.current_data()

    next_prev = p.next_prev()

    showpages = [x for x in range(1,showpages+1)]
    results = results[sn[0]:sn[1]]#当前页展示书籍，从第几本开始，到第几本结束
    print(results)
    context = {'book': results,'showpages':showpages,'current_page':current_page,
               'next_prev':next_prev,'total_pages':total_pages,'keyword':keyword
               }
    #返回的是当前页的数据数量
    return render(request, 'booklist/search_results.html', context)


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


def layout(request):
    return render(request, 'booklist/layout.html')


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
