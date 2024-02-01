from rest_framework import serializers

from news.models import News


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields: tuple[str] = ('id', 'title', 'image', 'description')


class NewsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields: str = '__all__'
