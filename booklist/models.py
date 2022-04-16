from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    # writer = models.CharField(max_length=20)
    press = models.CharField(max_length=20)
    date = models.DateField('出版日期')

    def __str__(self):
        return self.title


class Writer(models.Model):
    wname = models.CharField(max_length=20)
    wage = models.IntegerField()


class book_writer(models.Model):
    bid = models.IntegerField()
    wid = models.IntegerField()


class Organization(models.Model):
    orgname = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    scale = models.IntegerField(default=0)
    established_time = models.DateField('成立时间')

    def __str__(self):
        return self.name


class Hero(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, db_column='hname')
    skill = models.CharField(max_length=20)

    # org = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)
