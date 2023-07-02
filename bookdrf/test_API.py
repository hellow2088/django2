import requests
import json

# 1.get all books
# r = requests.get('http://127.0.0.1:8000/bookdrf/books')
r = requests.get('https://www.runoob.com/try/ajax/json_demo.json')


'''2.添加书籍-add a book'''
data = {
    # "id":11,
    "title": "HTML",
    "writer":"Tok",
    "press": "Press01",
    "pub_date": "2021-06-01",
    # "is_delete":0
}
# data = json.dumps(data)#view 使用序列化器，已经调用duoms，请求前不需要再次序列化
# r = requests.post('http://127.0.0.1:8000/bookdrf/books',data=data)

'''修改数据'''
# r = requests.put('http://127.0.0.1:8000/bookdrf/books_get/1',data=data)

# 3.获取一本书
# 3.get a book
# r = requests.get('http://127.0.0.1:8000/bookdrf/books_get/2')



# 5.delete
# r = requests.delete('http://127.0.0.1:8000/bookdrf/books_get/1')

# print(r.text)
# rt = json.loads("%s" %r.text)
# print(rt)

# print(data.get['title'])

'''WriterSerializers test'''
# 1.get all orgs
# r = requests.get('http://127.0.0.1:8000/bookdrf/org')

#2.添加org,add a org
# data = {
#     "orgname":"华山派",
#     "district":"华山",
#     "scale":"500",
#     "established_time":"0500-02-02"
# }
# data = json.dumps(data)
# r = requests.post('http://127.0.0.1:8000/bookdrf/org',data=data)


# 3.获取一本书
# 3.get a book
# r = requests.get('http://127.0.0.1:8000/bookdrf/books_get/7')

# 4.修改,modify
# data = {
#     "title":"C++",
#     "writer":"本书编写组",
#     "press": "科学出版社",
#     "date":"2020-09-23"
#
# }
# data = json.dumps(data)
# r = requests.put('http://127.0.0.1:8000/bookdrf/books_get/1',data=data)

# 5.delete
# r = requests.delete('http://127.0.0.1:8000/bookdrf/books_get/7')


'''HeroSerializer test'''
# 1.get all heros
# r = requests.get('http://127.0.0.1:8000/bookdrf/hero')

# 2.添加hero
# data = {
#     "book":"60",
#     "org":"1",
#     "name":"Ken",
#     "skill":"fly"
# }
# data = json.dumps(data)
# r = requests.post('http://127.0.0.1:8000/bookdrf/hero',data=data)


# 3.获取一本书
# 3.get a book
# r = requests.get('http://127.0.0.1:8000/bookdrf/books_get/7')

# 4.修改,modify
# data = {
#     "title":"C++",
#     "writer":"本书编写组",
#     "press": "科学出版社",
#     "date":"2020-09-23"
#
# }
# data = json.dumps(data)
# r = requests.put('http://127.0.0.1:8000/bookdrf/books_get/1',data=data)

# 5.delete
# r = requests.delete('http://127.0.0.1:8000/bookdrf/books_get/7')













# print('response.text',r.text,'\n')
# rt = json.loads("%s" %r.text)
# rt = json.loads(r.text)
print(r.text)

# print(data.get['title'])
