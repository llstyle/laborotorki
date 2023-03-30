from rest_framework import routers
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = routers.SimpleRouter()
router.register(r'api/v1/blog',  views.BlogViewSet)
router.register(r'api/v1/blogCreate',  views.BlogCreateViewSet)
router.register(r'api/v1/reviewCreate',  views.ReviewCreateViewSet)

urlpatterns = [
    path('', views.main),
    path('profile/', views.profile),
    path('create/', views.create),
    path('about/', views.about),
    path('', include(router.urls)),
    path('api/v1/blog/author/<slug:slug>/', views.BlogAuthorViewSet.as_view()),
    path('blog/<int:pk>/', views.Blog_Detail.as_view()),
]
urlpatterns += router.urls