# class Student():
#     def __init__(self, name, results):
#         self.name = name
#         for key, value in results.items():
#             setattr(self, key, value)
#
#     def update_mark(self, subject, mark):
#         self.subject = mark
#
#
#     def getScore(self):
#         print(self.en)
#
# s = Student('kk',{'en':'100'})
# print(s.name)
# print(s.getScore())

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    self.color = 'black'

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, age,fname, lname):
    Person.__init__(self, fname, lname)
    self.age = age

s = Student(12,'Fname','lname')
print(s.age)
print(s.color)
s.printname()