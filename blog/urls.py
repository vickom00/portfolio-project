from django.urls import path
from . import views

urlpatterns = [
    path('', views.content, name='content'),
    path('<int:blog_id>/', views.details, name='details')
]