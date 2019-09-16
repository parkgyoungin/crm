from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('<str:model>/write', views.write, name='write'),
    path('<str:model>/update/<int:id>', views.update, name='update'),
    path('<str:model>/list', views.list, name='list'),
    path('<str:model>/detail/<int:id>', views.detail, name='detail'),
    path('check/bnumber', views.check_bnumber, name='check_bnumber'),
    path('check/ips', views.check_ips, name='check_ips'),
]