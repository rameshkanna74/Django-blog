from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from markdown import markdown
from django.utils import timezone
from django.urls import reverse

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


# Post Model
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")  # Added related_name for clarity
    content = models.TextField(help_text="Write your blog post using Markdown.")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="posts", blank=True)  # `blank=True` to allow empty categories
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def get_markdown(self):
        return markdown(self.content, extensions=["fenced_code", "codehilite"])  # Added useful Markdown extensions

    @property
    def is_published(self):
        return self.published_at is not None and self.published_at <= timezone.now()

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def unpublish(self):
        self.published_at = None
        self.save()

    class Meta:
        ordering = ['-created_at']  # Newest posts first


# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

    class Meta:
        ordering = ['created_at']  # Oldest comments first


# Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    posts = models.ManyToManyField(Post, related_name="tags", blank=True)  # Added `posts` relationship for tagging posts

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})


# BlogImage Model
class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog_media/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or f"Image {self.id}"
