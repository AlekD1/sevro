from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from news.models import News
from news.serializers import NewsListSerializer, NewsRetrieveSerializer


class NewsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_classes = {
        'list': NewsListSerializer,
        'retrieve': NewsRetrieveSerializer,
    }
    queryset = News.objects.all()
    default_serializer_class = NewsListSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
