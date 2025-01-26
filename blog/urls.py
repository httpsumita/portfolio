from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name='bloghome'),
    path('<str:pk>',views.blogpost,name='blogpost')
]