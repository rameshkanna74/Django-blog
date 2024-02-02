from django.shortcuts import render, redirect
from .forms import PostCreateForm
from .models import Post

# Create your views here.
# def home_view(request):
#     return render(request, "1_base.html",)


def home_view(request):
    print("home_view", request)
    print(request.method)
    # print(request.META)
    if request.method == "POST":
        print("Bye Bye")
    posts = Post.objects.all()
    return render(request, "a_posts/home.html", {"posts": posts})


def post_create_view(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "a_posts/post_create.html", {"form": form})
