from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
    
    path('demo_http_response/', views.demo_http_response, name='demo_http_response')
]
