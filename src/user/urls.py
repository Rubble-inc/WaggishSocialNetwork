from django.urls import path
from .views import register, authorization, logout_user
urlpatterns = [

    path('user/register', register, name='reg'),
    path('user/auth', authorization, name='login'),
    path('user/logout', logout_user, name='logout'),

]


