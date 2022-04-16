from django.db import models

# Create your models here.

class Group(models.Model):
    gname = models.CharField(max_length=20)

    def __str__(self):
        return self.gname,self.id

class User(models.Model):
    username = models.CharField(max_length=50,default='Jone')
    nickname = models.CharField(max_length=50,default='Jone')
    password = models.CharField(default='123',max_length=50)
    gender = models.IntegerField(default='12')
    group = models.ManyToManyField(Group)
    email = models.CharField(default='123@126.com',max_length=100)

    def __str__(self):
        return self.username

    #     insert into useradmin_user values(1,'hud','hud','admin','1','1','hud@admin.com');
    #     insert into useradmin_group('emp');

