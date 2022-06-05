from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexblog, name='indexblog')
]