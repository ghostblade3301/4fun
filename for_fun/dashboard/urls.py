from django.urls import path

from . import views


app_name = 'dashboard'


urlpatterns = [
    path('', views.index, name='index'),
    path('group_list', views.group_posts, name='group_list'),
]
