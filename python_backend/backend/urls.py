from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:chai_id>/', views.desc, name='desc'),
    path('price/<int:chai_id>/', views.prices, name='prices')
]