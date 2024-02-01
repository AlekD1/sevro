from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from feedback.models import Feedback
from feedback.serializers import FeedbackSerializer


class FeedbackViewsSet(mixins.CreateModelMixin,
                       GenericViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
