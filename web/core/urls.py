from django.urls import path

from .views import get_vision_data, home, index

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("get_vision_data/", get_vision_data, name="get_vision_data"),
    path("accounts/profile/", home),
]
