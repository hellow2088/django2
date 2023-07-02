from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    writer = models.CharField(max_length=30,default='无名氏')
    press = models.CharField(max_length=20)
    pub_date = models.DateField('出版日期')
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Organization(models.Model):
    orgname = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    scale = models.IntegerField(default=0)
    established_time = models.DateField('成立时间')
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Hero(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, db_column='hname')
    skill = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)

    # org = models.CharField(max_length=20)

    def __str__(self):
        return self.name

