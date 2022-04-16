class Animal():
    def __init__(self,color):
        self.name = 'Fod'
        self.color = color

    def eat(self):
        print('eating')

class Dog(Animal):
    def __init__(self,age,color):
        super().__init__(color)
        self.age = age

    def bark(self):
        print('barking')
        l = [5,1,2,3,4]
        print(l)
        l1 = sorted(l)
        print(l1)
        # for i in l1:
        #     print(i)

d = Dog(4,'black')
print('name--%s'%d.name)
print('color--%s'%d.color)
print('age--%s'%d.age)
d.eat()
print(d.bark())

# a = Animal('green')
# print(a.color)
# print(a.name)