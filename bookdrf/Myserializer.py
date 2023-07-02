from rest_framework import serializers
from .models import Book

# 序列化器
class BookSerializer(serializers.ModelSerializer):
    # title = serializers.CharField()
    # writer = serializers.CharField()
    # press = serializers.CharField()
    # pub_date = serializers.DateField()

    class Meta:
        model = Book
        fields = '__all__'