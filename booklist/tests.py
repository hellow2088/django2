from django.test import TestCase

class BaseAnimal(object):
    def __init__(self,height):
        # setattr(height)
        self.height = height
        # for k,v in kwargs.items():
        #     print(k,'--',v)
        #     setattr(k,v)

    def eat(self,*args):
        print('eating %s'%args[1])

    # def eat2():
    #     print('eating')


class Mammal(BaseAnimal):
    def __init__(self,age):
        super(BaseAnimal,self).__init__()
        self.age = age


class Dog(Mammal):
    pass

d = Dog(10)
setattr(d,'name','kl')
print(d.name)
print(d.age)
# print(d.height)
d.eat('meat','apple')

