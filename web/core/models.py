from uuid import uuid4

from django.db import models


class DocumentData(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, unique=True, primary_key=True)
    image_name = models.CharField(max_length=100)
    ocr_text = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

class DocumentColumn(models.Model):
    document_data = models.ForeignKey(to=DocumentData, on_delete=models.CASCADE)
    noms = models.CharField(max_length=50)
    pnoms = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    corps = models.CharField(max_length=50)
    first_date = models.CharField(max_length=20)
    last_date = models.CharField(max_length=20)
    numero = models.CharField(max_length=50)
