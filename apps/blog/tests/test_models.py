import pytest
from django.utils import timezone
from apps.blog.models import Category, Post, Comment, Tag
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_category_slug_creation():
    category = Category.objects.create(name="Django Testing")
    assert category.slug == "django-testing"


@pytest.mark.django_db
def test_post_slug_creation():
    user = User.objects.create_user(username="testuser", password="password")
    post = Post.objects.create(
        title="My First Post", author=user, content="Hello, World!"
    )
    assert post.slug == "my-first-post"


@pytest.mark.django_db
def test_post_markdown_rendering():
    user = User.objects.create_user(username="testuser", password="password")
    post = Post.objects.create(
        title="Markdown Post", author=user, content="# Header\nSome **bold** text."
    )
    rendered = post.get_markdown()
    assert "<h1>Header</h1>" in rendered
    assert "<strong>bold</strong>" in rendered


@pytest.mark.django_db
def test_post_is_published_property():
    user = User.objects.create_user(username="testuser", password="password")
    post = Post.objects.create(
        title="Publish Test", author=user, content="Test Content"
    )
    assert post.is_published is False

    post.publish()
    assert post.is_published is True


@pytest.mark.django_db
def test_post_publish_method():
    user = User.objects.create_user(username="testuser", password="password")
    post = Post.objects.create(
        title="Publish Test", author=user, content="Test Content"
    )
    assert post.published_at is None

    post.publish()
    assert post.published_at is not None
    assert post.is_published is True


@pytest.mark.django_db
def test_post_unpublish_method():
    user = User.objects.create_user(username="testuser", password="password")
    post = Post.objects.create(
        title="Unpublish Test", author=user, content="Test Content"
    )
    post.publish()
    assert post.is_published is True

    post.unpublish()
    assert post.is_published is False


@pytest.mark.django_db
def test_comment_creation():
    user = User.objects.create_user(username="testuser", password="password")
    post = Post.objects.create(
        title="Post for Comments", author=user, content="Content"
    )
    comment = Comment.objects.create(
        post=post, author="Commenter", content="This is a comment."
    )
    assert comment.post == post
    assert comment.author == "Commenter"
    assert comment.content == "This is a comment."


@pytest.mark.django_db
def test_tag_slug_creation():
    tag = Tag.objects.create(name="Django")
    assert tag.slug == "django"


@pytest.mark.django_db
def test_post_tag_association():
    user = User.objects.create_user(username="testuser", password="password")
    post = Post.objects.create(title="Tagged Post", author=user, content="Content")
    tag = Tag.objects.create(name="Django")
    post.tags.add(tag)

    assert tag in post.tags.all()
    assert post in tag.posts.all()
