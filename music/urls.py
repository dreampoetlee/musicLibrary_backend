from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_library),
    path('<int:pk>/', views.song_detail)
]
