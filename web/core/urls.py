from django.urls import path

from .views import edit_document, home, index

urlpatterns = [
    path("", index),
    path("accounts/profile/", home),
    path("edit_document/<uuid:document_id>/", edit_document, name="edit_document"),
]
