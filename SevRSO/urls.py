import rest_framework.routers
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from album.views import AlbumViewSet
from feedback.views import FeedbackViewsSet
from news.views import NewsViewSet
from secondaryinfo.views import QAAPIView, StatisticListAPIView, ProjectViewSet, ContactListViewSet, DocumentViewSet, \
    PartnerListAPIView
from squad.views import SquadViewSet, FiguresListAPIView, DirectionViewSet
from .yasg import urlpatterns as doc_urls

router = rest_framework.routers.SimpleRouter()
router.register('direction', DirectionViewSet, basename='direction')
router.register('album', AlbumViewSet, basename='album')
router.register('project', ProjectViewSet, basename='project')
router.register('squad', SquadViewSet, basename='squad')
router.register('document', DocumentViewSet, basename='document')
router.register('news', NewsViewSet, basename='news')
router.register(r'qa', QAAPIView)
router.register(r'feedback', FeedbackViewsSet)
router.register(r'contacts', ContactListViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('editor/', include('django_summernote.urls')),
    path('api/', include(router.urls)),
    path('api/statistic/', StatisticListAPIView.as_view()),
    path('api/figures/', FiguresListAPIView.as_view()),
    path('api/partners/', PartnerListAPIView.as_view()),
]

urlpatterns += doc_urls
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)