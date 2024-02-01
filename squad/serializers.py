from rest_framework import serializers

from album.models import Album
from album.serializers import AlbumRetrieveSerializer
from squad.models import Squad, Figure, Position, Direction


class SquadListSerializer(serializers.ModelSerializer):
    direction = serializers.StringRelatedField()
    class Meta:
        model = Squad
        fields: tuple[str] = (
            'id',
            'name',
            'direction',
            'main_image',
            'description',
            'vk'
        )


class SquadRetrieveSerializer(serializers.ModelSerializer):
    figures = serializers.SerializerMethodField()
    albums = serializers.SerializerMethodField()
    direction = serializers.StringRelatedField()

    class Meta:
        model = Squad
        fields = '__all__'

    @staticmethod
    def get_figures(obj):
        queryset = Figure.objects.prefetch_related('squad_important_people').filter(squad_important_people=obj)
        print(queryset)
        return [FigureSerializer(q).data for q in queryset]

    @staticmethod
    def get_albums(obj):
        queryset = Album.objects.prefetch_related('squad_albums').filter(squad_albums=obj)
        return [AlbumRetrieveSerializer(q).data for q in queryset]


class FigureSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    class Meta:
        model = Figure
        fields: str = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields: str = '__all__'


class DirectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields: tuple[str] = ('id', 'name', 'main_image', 'icon', 'description')


class DirectionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields: str = '__all__'
