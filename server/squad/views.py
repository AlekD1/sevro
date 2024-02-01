from squad.models import Squad, Figure
from squad.serializers import SquadRetrieveSerializer, SquadListSerializer, FigureSerializer
from rest_framework import generics, viewsets

from .models import Direction
from .serializers import DirectionListSerializer, DirectionRetrieveSerializer
from mixins.viewset_mixins import SerializerClassesMixin


class SquadViewSet(SerializerClassesMixin, viewsets.ReadOnlyModelViewSet):
    LIST = SquadListSerializer
    RETRIEVE = SquadRetrieveSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        direction_id = self.request.query_params.get('direction_id', None)
        if direction_id is not None:
            queryset = queryset.filter(direction_id=direction_id)
        return queryset

    queryset = Squad.objects.select_related('direction').prefetch_related('albums', 'figures').all()


class FiguresListAPIView(generics.ListAPIView):
    queryset = Figure.objects.select_related('position').filter(on_main=True)
    serializer_class = FigureSerializer


class DirectionViewSet(SerializerClassesMixin, viewsets.ReadOnlyModelViewSet):
    """
    Данный ViewSet позволяет использовать только метод GET,
    отдавая объект(ы) в формате, который определен в пути к нему же.
    В ReadOnlyModelViewSet уже реализован list() и retrieve()
    """
    LIST = DirectionListSerializer
    RETRIEVE = DirectionRetrieveSerializer
    queryset = Direction.objects.all()
