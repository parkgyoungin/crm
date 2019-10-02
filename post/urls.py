from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('<str:model>/write/', views.write, name='write'),
    path('<str:model>/update/<int:pk>/', views.update, name='update'),
    path('<str:model>/list/', views.list, name='list'),
    path('<str:model>/detail/<int:pk>/', views.detail, name='detail'),
    path('<str:model>/delete/<int:pk>/', views.delete, name='delete'),
    path('check/<str:model>/<str:field_name>/<str:ele_id>/', views.check, name='check'),
    path('search/<str:model>/<str:field_name>/', views.search, name='search'),
    path('select/<str:model>/<int:id>/', views.select, name='select')
]