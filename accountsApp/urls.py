from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views
from .views import *
urlpatterns = [
    path("home/",views.home,name="home"),
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='pages/home.html'),name='logout'),
    path('goals/<id>',views.showGoals,name='showgoal'),
    path('goals/<int:id>/addgoal',views.addGoal,name='addGoal'),
    path('goals/<int:id>/update',views.editGoal,name='edit'),
    path('goals/<int:id>/delete', views.deleteGoal,name="delete"),
]