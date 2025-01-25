from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('story/<str:genre>/', views.story, name='story'),
    path('api/story/<str:genre>/', views.get_story, name='get_story'),
]
