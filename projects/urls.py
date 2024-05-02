from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register/', views.registerUser, name='register'),
    path('customer_review/', views.customer_review, name='customer_review'),
    path('customer_add/', views.customer_add, name='customer_add'),

]