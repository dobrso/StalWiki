from django.urls import path

from . import views

app_name = 'guides'

urlpatterns = [
    path('', views.guide_list, name='guide_list'),
    path('create/', views.guide_create, name='guide_create'),
    path('detail/<int:guide_id>/', views.guide_detail, name='guide_detail'),
]