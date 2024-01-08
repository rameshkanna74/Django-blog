from django.urls import path
from .views import home, login_t, logout_t, signup

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("login_t/", login_t, name="login_t"),
    path("logout_t/", logout_t, name="logout_t"),
]
