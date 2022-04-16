from django.contrib.auth.models import AbstractUser
from django.db import models


class UserInfo(AbstractUser):
    uid = models.AutoField(primary_key=True)
    tel = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to='avaters/', default='/avatar/default.png')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    blog = models.OneToOneField(to='Blog', to_field='bid', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Blog(models.Model):
    bid = models.AutoField(primary_key=True)
    btitle = models.CharField(verbose_name='个人博客标题', max_length=64)
    site_name = models.CharField(verbose_name='站点名称', max_length=64)
    theme = models.CharField(verbose_name='博客主题', max_length=32)

    def __str__(self):
        return self.btitle


class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    ctitle = models.CharField(verbose_name='分类标题', max_length=32)
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='bid', on_delete=models.CASCADE)

    def __str__(self):
        return self.ctitle


class Tag(models.Model):
    tid = models.AutoField(primary_key=True)
    ttitle = models.CharField(verbose_name='标签名称', max_length=32)
    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='bid', on_delete=models.CASCADE)

    def __str__(self):
        return self.ttitle


class Article(models.Model):
    aid = models.AutoField(primary_key=True)
    atitle = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(verbose_name='文章简介', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    content_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)

    user = models.ForeignKey(verbose_name='作者', to='UserInfo', to_field='uid',on_delete=models.CASCADE)
    category = models.ForeignKey(to="Category", to_field='cid',on_delete=models.CASCADE)
    tags = models.ManyToManyField(to='Tag', through='Article2Tag', through_fields=('article', 'tag'))

    def __str__(self):
        return self.atitle


class Article2Tag(models.Model):
    atid = models.AutoField(primary_key=True)
    article = models.ForeignKey(verbose_name='文章标题', to='Article', to_field='aid',on_delete=models.CASCADE)
    tag = models.ForeignKey(verbose_name='标签', to='Tag',to_field='tid',on_delete=models.CASCADE)

    class Meta:
        unique_together = [('article', 'tag')]

    def __str__(self):
        v = self.article.atitle + '--' + self.tag.ttile
        return v


class ArticleUpDown(models.Model):
    udnid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to='UserInfo', to_field='uid',on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article', to_field='aid',on_delete=models.CASCADE)
    is_up = models.BooleanField(default=True)

    class Meta:
        unique_together = [('article', 'user')]


class Comment(models.Model):
    cmid = models.AutoField(primary_key=True)
    article = models.ForeignKey(verbose_name='评论文章', to='Article', to_field='aid',on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='作者', to='UserInfo', to_field='uid',on_delete=models.CASCADE)
    content = models.CharField(verbose_name='评论内容', max_length=255)
    create_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.content
