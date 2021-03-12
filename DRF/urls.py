from django.urls import path, include
from knox import views as knox_views
from DRF.api import *#LoginView, RegisterUser, RegisterDonor, RegisterNGOAdmin, UserDisplayView
from rest_framework import routers






urlpatterns = [

    path('users-display/', UserDisplayView.as_view(), name='user-display-all'),
    path('users-display/<int:pk>/', UserDisplayView.as_view(), name='user-display-single'),

    path('donors-display/', DonorDisplayView.as_view(), name='donor-display-all'),
    path('donors-display/<int:pk>/', DonorDisplayView.as_view(), name='donor-display-single'),

    path('ngo-admin-display/', NGOAdminDisplayView.as_view(), name='ngo-admin-display-all'),
    path('ngo-admin-display/<int:pk>/', NGOAdminDisplayView.as_view(), name='ngo-admin-display-single'),

    path('user-register/', RegisterUser.as_view(), name='user-register'),
    path('donor-register/', RegisterDonor.as_view(), name='donor-register'),
    path('ngo-admin-register/', RegisterNGOAdmin.as_view(), name='ngo-admin-register'),


    path('', include('rest_framework.urls')),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),

]
