from django.urls import path

from . import views

app_name = 'guides'

urlpatterns = [
    path('guides/', views.guide_list, name='guide_list'),
]