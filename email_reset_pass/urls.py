from django.urls import path
from .views import login,logout,signup,home

urlpatterns=[
    path('',home, name="home"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('signup/',signup,name="signup"),

]