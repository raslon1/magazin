from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    guid = serializers.UUIDField()
    parent = serializers.UUIDField()


class ProductsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    guid = serializers.UUIDField()
    color = serializers.CharField()
    category = serializers.CharField()
    price = serializers.IntegerField(min_value = 0)