import json
from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import DocumentForm
from .models import DocumentData


def get_vision_data(request):
    vision_data = [
        {"label": "Water", "score": 0.9796228408813477},
        {"label": "Building", "score": 0.9618409872055054},
        {"label": "Water resources", "score": 0.948203444480896},
        {"label": "Skyscraper", "score": 0.9370574951171875},
        {"label": "Plant", "score": 0.9085065722465515},
        {"label": "Tower", "score": 0.8631998896598816},
        {"label": "Tower block", "score": 0.8545447587966919},
        {"label": "Urban design", "score": 0.8416244983673096},
        {"label": "Body of water", "score": 0.8403213024139404},
        {"label": "Coastal and oceanic landforms", "score": 0.8392763733863831},
    ]
    return JsonResponse(vision_data, safe=False)


def home(request):
    return render(request, "base.html")


@login_required(login_url="accounts/login")
def index(request, id: uuid4 = None):
    document_data = DocumentData.objects.all()
    json_data = []
    if id:
        document_instance = DocumentData.objects.get(id=id)
        json_data = document_instance.ocr_json
        for key, value in json_data.items():
            print(f"{key}: {value}")

    vision_data = [
        {"label": "Water", "score": 0.9796228408813477},
        {"label": "Building", "score": 0.9618409872055054},
        {"label": "Water resources", "score": 0.948203444480896},
        {"label": "Skyscraper", "score": 0.9370574951171875},
        {"label": "Plant", "score": 0.9085065722465515},
        {"label": "Tower", "score": 0.8631998896598816},
        {"label": "Tower block", "score": 0.8545447587966919},
        {"label": "Urban design", "score": 0.8416244983673096},
        {"label": "Body of water", "score": 0.8403213024139404},
        {"label": "Coastal and oceanic landforms", "score": 0.8392763733863831},
    ]

    if request.headers.get("HX-Request"):
        # Handle htmx request
        vision_data = get_updated_vision_data()
        context = {"vision_data": vision_data}
        html_content = render_to_string("partial_vision_data.html", context)
        return JsonResponse({"html": html_content})
    context = {"document_data": document_data, "vision_data": vision_data}
    return render(request, "index.html", context)
