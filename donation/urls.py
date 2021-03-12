from donation.views import register_donation, display_donation, display_donated_by, register_donated_by
from django.urls import include, path

urlpatterns = [

    path('register-donation/', register_donation, name = 'register-donation'),
    path('register-donated-by/', register_donated_by, name = 'register-donated-by'),
    path('display-donation/', display_donation, name='display_donation'),
    path('display-donated-by/', display_donated_by, name='display_donated_by')

]