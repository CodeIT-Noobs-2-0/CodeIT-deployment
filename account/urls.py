from .views import *
from django.urls import include, path
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from account import views

urlpatterns = [

    path('',views.index, name='index'),
    path('signup/', views.donorSignup, name='signup'),
    path('ngoadminSignup/', views.ngo_adminSignup, name='ngoAdminSignup'),
    path('login/', auth_views.LoginView.as_view(),{'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': 'index'}, name='logout'),

]