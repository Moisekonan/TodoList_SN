from django.urls import path

# TODO: use this, form application import file or for application.file import fuction or class
# Example: for authen import views
# In your cas, from authen.views import login_view, register, logout_view
from authen.views import login_view, register, logout_view

urlpatterns = [
    
    path('', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
]
