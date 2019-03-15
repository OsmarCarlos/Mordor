from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import kingdom_places, HobbitViewSet
router = DefaultRouter()

router.register('hobbits', HobbitViewSet)

urlpatterns = [
    # Router
    url(r'^', include(router.urls)),
    url(r'kingdom_places', kingdom_places),
    # Admin
]