from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from mixins.viewset_mixins import SerializerClassesMixin
from secondaryinfo.models import Statistic, QA, Project, Document, Contact, Partner
from secondaryinfo.serializers import QASerializer, StatisticSerializer, ProjectListSerializer, \
    ProjectRetrieveSerializer, \
    DocumentSerializer, CustomContactSerializer, PartnerSerializer


class StatisticListAPIView(generics.ListAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer


class QAAPIView(mixins.ListModelMixin,
                GenericViewSet):
    queryset = QA.objects.all()
    serializer_class = QASerializer


class ProjectViewSet(SerializerClassesMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.prefetch_related('images').all()
    LIST = ProjectListSerializer
    RETRIEVE = ProjectRetrieveSerializer


class DocumentViewSet(SerializerClassesMixin, viewsets.ReadOnlyModelViewSet):
    LIST = DocumentSerializer
    RETRIEVE = DocumentSerializer
    queryset = Document.objects.all()


class ContactListViewSet(mixins.ListModelMixin,
                GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = CustomContactSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {}
        for item in serializer.data:
            data.update(item)
        return Response(data)


class PartnerListAPIView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer