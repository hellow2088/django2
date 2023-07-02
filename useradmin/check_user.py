from django.http import HttpResponse

from .models import User

def checkUser(username,pwd):

    check_result = {'check_result':'', 'msg':''}
    # 判断用户名是否重复
    try:
        u = User.objects.get(username=username)
    except:
        u = None

    if u:
        check_result['check_result'] = False
        check_result['msg'] = '用户名已存在'
        return check_result
    # 检查用户名是否合法
    sep_char = ['!', '#', '$', '%', '^', '&', '*', '(', ')']
    for schar in sep_char:
        if schar in username:
            check_result["check_result"] = False
            check_result['msg'] = '用户名不能含有特殊字符'
            return check_result
    # 密码是否包含字母
    has_char = False
    for i in range(65, 91):
        if chr(i) in pwd:
            has_char = True
    for i in range(97,122):
        if chr(i) in pwd:
            has_char = True
    if has_char != True:
        check_result["check_result"] = False
        check_result['msg'] = '密码必须包含字母'
        return check_result
    # 密码是否有数字
    has_num = False
    for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        if num in pwd:
            has_num = True
    if has_num != True:
        check_result["check_result"] = False
        check_result['msg'] = '密码必须包含数字'
        return check_result
    #检查用户名和密码长度
    if len(username) < 4 or len(username) > 16:
        check_result["check_result"] = False
        check_result['msg'] = '用户名长度大于5汉字小于16汉字'
        return check_result
    if len(pwd) < 6 or len(pwd) > 16:
        check_result["check_result"] = False
        check_result['msg'] = '密码长度不能小于6位或大于16位'
        return check_result