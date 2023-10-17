from django.urls import path
from Auth_App.views import *
urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile')
]