from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JournalEntryViewSet, PublicJournalEntryListView

router = DefaultRouter()
router.register('entries', JournalEntryViewSet, basename='entries')

urlpatterns = [
    path('', include(router.urls)),
    path('journal/public/', PublicJournalEntryListView.as_view()),
]