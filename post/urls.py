from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('<str:model>/write', views.write, name='write'),
    path('<str:model>/update/<int:pk>', views.update, name='update'),
    path('<str:model>/list', views.list, name='list'),
    path('<str:model>/detail/<int:pk>', views.detail, name='detail'),
    path('check/<str:model>/<str:field_name>/<str:ele_id>', views.check, name='check')
]