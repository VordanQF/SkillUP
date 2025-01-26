from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.profile, name='about'),
    path('glav', views.glav, name='glav'),
    path('sovet', views.sovet, name='sovet'),
    path('recept', views.recept, name='recept'),
    path('login', views.login, name='login')
]