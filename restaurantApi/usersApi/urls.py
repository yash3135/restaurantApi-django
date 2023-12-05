from django.urls import path
from . import views

urlpatterns = [
    path('users', views.userApi),
    path('users/<int:id>', views.userApi)
]