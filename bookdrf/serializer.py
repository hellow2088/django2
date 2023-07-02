from rest_framework import serializers


class OrganizationSerializer(serializers.Serializer):
    orgname = serializers.CharField()
    district = serializers.CharField()
    scale = serializers.IntegerField()
    established_time = serializers.DateField()


# 序列化器
class HeroSerializer(serializers.Serializer):
    '''read_only 不参与验证，write_only 只反序列化'''
    name = serializers.CharField(read_only=False,write_only=False,max_length=20,min_length=5)
    skill = serializers.CharField()
    book_id = serializers.IntegerField()
    org_id = serializers.IntegerField()
    # book_set = serializers.StringRelatedField()
    book_set = serializers.PrimaryKeyRelatedField(read_only=True)

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20,min_length=5)
    writer = serializers.CharField(required=True)
    # Writer_set = WriterSerializer(many=True)
    press = serializers.CharField()
    date = serializers.DateField()
    '''返回关联hero id'''
    # hero_set =serializers.PrimaryKeyRelatedField(read_only=True,many=True)

    '''返回model str 值'''
    # hero_set =serializers.StringRelatedField(read_only=True,many=True)

    '''
    required=True,添加书籍后，要返回hero信息，此时新book没有hero信息，会报错，
    required=False避免这个错误
    '''
    hero_set = HeroSerializer(many=True,required=False)
