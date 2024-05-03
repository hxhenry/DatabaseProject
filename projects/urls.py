from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('customer_review/', views.customer_review, name='customer_review'),
    path('customer_add/', views.customer_add, name='customer_add'),
]
