from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('join', views.join, name='join'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('check/userid', views.check_userid, name='check_userid'),
    path('check/nickname', views.check_nickname, name='check_nickname'),
    path('confirm_password', views.confirmPassword, name='confirm_password'),
    path('update_user', views.updateUser, name='update_user'),
]