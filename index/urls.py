from . import views
from django.urls import path

app_name ='index'

urlpatterns = [
    path('top/', views.index, name='index'),
]