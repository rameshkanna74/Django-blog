# forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import DocumentData


class CustomSignUpForm(UserCreationForm):
    # Customize the form if needed
    pass


class CustomAuthenticationForm(AuthenticationForm):
    # Customize the form if needed
    pass


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentData
        fields = [
            "image_name",
            "ocr_text",
        ]
