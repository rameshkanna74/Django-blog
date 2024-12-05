from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse
from .models import Post, Category, Tag, Comment
from .forms import PostForm, CommentForm
from markdown import markdown

# List all posts (Home page)
def post_list(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('-created_at')  # Published posts only
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'blog/post_list.html', context)

# Display a single post
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.order_by('created_at')  # Fetch comments ordered by creation time
    post_content_html = markdown(post.content)  # Render Markdown to HTML

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user.username
            comment.save()
            messages.success(request, 'Your comment has been posted!')
            return redirect('post_detail', slug=slug)  # Avoid duplicate comment submission
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'post_content_html': post_content_html,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)

# Category-based post listing
def post_list_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(published_at__lte=timezone.now()).order_by('-created_at')

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/post_list_by_category.html', context)

# Tag-based post listing
def post_list_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags__slug=tag.slug, published_at__lte=timezone.now()).order_by('-created_at')

    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'blog/post_list_by_tag.html', context)

# Create a new post
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Save many-to-many data for categories and tags
            messages.success(request, 'Your post has been created successfully!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()

    context = {
        'form': form,
        'action': 'Create',
    }
    return render(request, 'blog/post_form.html', context)

# Edit an existing post
@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        return HttpResponseForbidden('You do not have permission to edit this post.')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            form.save_m2m()  # Save many-to-many data
            messages.success(request, 'Your post has been updated successfully!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'action': 'Edit',
    }
    return render(request, 'blog/post_form.html', context)

# Delete a post
@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        return HttpResponseForbidden('You do not have permission to delete this post.')

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted!')
        return redirect('post_list')

    context = {
        'post': post,
    }
    return render(request, 'blog/post_confirm_delete.html', context)

# Publish a post (Admin or Author only)
@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        return HttpResponseForbidden('You do not have permission to publish this post.')

    post.publish()
    messages.success(request, f'{post.title} has been published!')
    return redirect('post_detail', slug=slug)

# Unpublish a post (Admin or Author only)
@login_required
def post_unpublish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        return HttpResponseForbidden('You do not have permission to unpublish this post.')

    post.unpublish()
    messages.success(request, f'{post.title} has been unpublished.')
    return redirect('post_detail', slug=slug)
