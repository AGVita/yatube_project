from django.urls import path

from . import views

app_name = 'posts'


urlpatterns = [
    path('', views.index, name='general_page'),
    # path('index.html', views.index, name='genera_page'),
    path('group_list.html', views.group_posts, name='group_page'),
    path('group/', views.general_page, name='group_page'),
]