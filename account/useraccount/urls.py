from django.urls import path
from . import views
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)


urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.index, name='index'),
    path('login/', login, {'template_name': 'useraccount/login.html'}),
    path('logout/', logout, {'template_name': 'useraccount/logout.html'}),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/changepassword/', views.change_password, name='change_password'),
    path('reset-password/', password_reset, name='reset_password'),
    path('done/', password_reset_done, name='password_reset_done'),
    path('confirm/', password_reset_confirm, name='password_reset_confirm'),
    path('complete/', password_reset_complete, name='password_reset_complete'),
    # 22
]
