from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

app_name = 'useraccount'
urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.index, name='index'),
    path('login/', login, {'template_name': 'useraccount/login.html'}),
    path('logout/', logout, {'template_name': 'useraccount.logout.html'}),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile')
    path('changepassword/', views.change_password, name='change_password')

]
