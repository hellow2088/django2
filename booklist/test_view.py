import requests
import json
# r = requests.get('http://127.0.0.1:8000/booklist/books_view')
# r = requests.get('https://www.runoob.com/try/ajax/json_demo.json')

data = {
    # "id":11,
    "title": "C++",
    "press": "清华大学出版社",
    "date": "2021-01-01"
}
data = json.dumps(data)
print(type(data))
r = requests.post('http://127.0.0.1:8000/booklist/books_view',data=data)

# r = requests.get('http://127.0.0.1:8000/booklist/books_get/7')


# data = {
#     "press": "科学出版社",
# }
# data = json.dumps(data)
# r = requests.put('http://127.0.0.1:8000/booklist/books_get/8',data=data)

# r = requests.delete('http://127.0.0.1:8000/booklist/books_get/3')

data = json.loads(r.text)
print(type(r.text))
print(data)

# print(data.get['title'])