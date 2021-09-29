
from django.urls import path
from . import views
app_name = 'movieapp'

urlpatterns = [

    path('', views.index1, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='details'),
    path('add/', views.add_movie, name='addmovie'),
    path('update/<int:id>/', views.change, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]
