from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteQuoteViewSet  # New ViewSet

router = DefaultRouter()
router.register(r'quotes', FavoriteQuoteViewSet)  # RESTful endpoints for FavoriteQuote

urlpatterns = [
    path('', include(router.urls)),  # Include all router endpoints
]
