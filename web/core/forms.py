# forms.py

from django import forms

from .models import DocumentData


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentData
        fields = [
            "image_name",
            "ocr_text",
        ]
