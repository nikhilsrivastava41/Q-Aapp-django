from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.queslist, name='queslist'),
    path('quesdetail/<int:id>', views.quesdetail, name='quesdetail'),
    path('ansdetail/<int:id>', views.ansdetail, name='ansdetail'),
    path('quesans', views.quesans, name='quesans'),
    path('askques', views.askques, name='askques'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]
