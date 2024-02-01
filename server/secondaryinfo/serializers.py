from rest_framework import serializers

from secondaryinfo.models import Statistic, QA, HomeSlider, Project, ProjectImage, Document, Contact, Partner


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        exclude: tuple[str] = ('id',)


class QASerializer(serializers.ModelSerializer):
    class Meta:
        model = QA
        exclude: tuple[str] = ('id',)


class HomeSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSlider
        exclude: tuple[str] = ('id',)


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields: tuple[str] = ('title', 'image')


class CustomContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['type', 'value']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {representation['type']: {'value': representation['value']}}


class ProjectListSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields: tuple[str] = (
            'title',
            'banner',
            'content',
            'images',
            'created_at'
        )

    @staticmethod
    def get_images(obj):
        queryset = ProjectImage.objects.filter(project=obj)
        return [ProjectImageSerializer(q).data for q in queryset]


class ProjectRetrieveSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields: tuple[str] = (
            'title',
            'banner',
            'content',
            'images',
            'created_at'
        )

    @staticmethod
    def get_images(obj):
        queryset = ProjectImage.objects.filter(project=obj)
        return [ProjectImageSerializer(q).data for q in queryset]


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields: tuple[str] = ('title', 'file', 'created_at')


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
