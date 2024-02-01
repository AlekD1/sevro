from rest_framework import serializers

from album.models import Album, AlbumImage


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model: Album = Album
        fields: tuple[str] = ('id', 'name', 'banner')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImage
        fields = ('image', 'title')


class AlbumRetrieveSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields: tuple[str] = ('id', 'name', 'banner', 'description', 'images')

    @staticmethod
    def get_images(obj):
        queryset = AlbumImage.objects.filter(album=obj)
        return [ImageSerializer(q).data for q in queryset]