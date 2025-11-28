from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('day/<int:day_id>/', views.day_detail, name='day_detail'),
]