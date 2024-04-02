from django.urls import path

# TODO: use this, form application import file or for application.file import fuction or class
# Example: for authen import views
# In your cas, from authen.views import login_view, register, logout_view
from . import views

urlpatterns = [
    
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
