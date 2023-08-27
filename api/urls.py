from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet
# from .views import article_list, article_details
router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, basename='article')
urlpatterns = [
    path('', include(router.urls))
    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details),
]