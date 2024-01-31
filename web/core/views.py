from django.shortcuts import redirect, render

from .forms import DocumentForm
from .models import DocumentData


def home(request):
    return render(request, "base.html")


def index(request):
    document_data = DocumentData.objects.all()
    return render(request, "index.html", {"document_data": document_data})


def edit_document(request, document_key):
    document_data = DocumentData.objects.get(pk=document_key)

    if request.method == "POST":
        form = DocumentForm(request.POST, instance=document_data)
        if form.is_valid():
            form.save()  # Save the updated document data
            return redirect("index")  # Redirect to the document list page
    else:
        form = DocumentForm(instance=document_data)

    return render(request, "index.html", {"form": form, "document_key": document_key})
