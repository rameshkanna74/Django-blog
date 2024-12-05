from django.urls import reverse
from django.test import TestCase

class BlogViewsTestCase(TestCase):
    def test_post_list(self):
        url = reverse('blog:post_list')  # Include 'blog' namespace
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_create(self):
        url = reverse('blog:post_create')  # Include 'blog' namespace
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


# from django.test import TestCase, Client
# from django.contrib.auth.models import User
# from django.urls import reverse
# from apps.blog.models import Post, Category, Tag, Comment
# from django.utils.timezone import now, timedelta


# class BlogViewsTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()

#         # Create test user
#         self.user = User.objects.create_user(username="testuser", password="password")

#         # Create another user
#         self.other_user = User.objects.create_user(
#             username="otheruser", password="password"
#         )

#         # Create categories and tags
#         self.category = Category.objects.create(
#             name="Test Category", slug="test-category"
#         )
#         self.tag = Tag.objects.create(name="Test Tag", slug="test-tag")

#         # Create posts
#         self.post = Post.objects.create(
#             title="Test Post",
#             slug="test-post",
#             content="This is a test post.",
#             author=self.user,
#             published_at=now() - timedelta(days=1),  # Published post
#         )
#         self.post.categories.add(self.category)
#         self.post.tags.add(self.tag)

#         self.draft_post = Post.objects.create(
#             title="Draft Post",
#             slug="draft-post",
#             content="This is a draft post.",
#             author=self.user,
#         )

#         # Create a comment
#         self.comment = Comment.objects.create(
#             post=self.post,
#             author="Anonymous",
#             content="This is a test comment.",
#         )

#     def test_post_list(self):
#         response = self.client.get(reverse("post_list"))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Test Post")
#         self.assertNotContains(response, "Draft Post")

#     def test_post_detail(self):
#         response = self.client.get(
#             reverse("post_detail", kwargs={"slug": self.post.slug})
#         )
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "This is a test post.")
#         self.assertContains(response, "This is a test comment.")

#     def test_post_detail_unauthenticated_comment(self):
#         response = self.client.post(
#             reverse("post_detail", kwargs={"slug": self.post.slug}),
#             data={"content": "New comment"},
#         )
#         self.assertEqual(
#             response.status_code, 200
#         )  # Comment form ignored for unauthenticated users

#     def test_post_detail_authenticated_comment(self):
#         self.client.login(username="testuser", password="password")
#         response = self.client.post(
#             reverse("post_detail", kwargs={"slug": self.post.slug}),
#             data={"content": "New authenticated comment"},
#         )
#         self.assertRedirects(
#             response, reverse("post_detail", kwargs={"slug": self.post.slug})
#         )
#         self.assertEqual(self.post.comments.count(), 2)

#     def test_post_list_by_category(self):
#         response = self.client.get(
#             reverse("post_list_by_category", kwargs={"slug": self.category.slug})
#         )
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Test Post")

#     def test_post_list_by_tag(self):
#         response = self.client.get(
#             reverse("post_list_by_tag", kwargs={"slug": self.tag.slug})
#         )
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Test Post")

#     def test_post_create(self):
#         self.client.login(username="testuser", password="password")
#         response = self.client.post(
#             reverse("post_create"),
#             data={
#                 "title": "New Post",
#                 "slug": "new-post",
#                 "content": "New post content",
#                 "categories": [self.category.id],
#                 "tags": [self.tag.id],
#             },
#         )
#         self.assertRedirects(
#             response, reverse("post_detail", kwargs={"slug": "new-post"})
#         )
#         self.assertTrue(Post.objects.filter(slug="new-post").exists())

#     def test_post_edit(self):
#         self.client.login(username="testuser", password="password")
#         response = self.client.post(
#             reverse("post_edit", kwargs={"slug": self.post.slug}),
#             data={
#                 "title": "Updated Test Post",
#                 "slug": "test-post",
#                 "content": "Updated content",
#             },
#         )
#         self.assertRedirects(
#             response, reverse("post_detail", kwargs={"slug": "test-post"})
#         )
#         self.post.refresh_from_db()
#         self.assertEqual(self.post.content, "Updated content")

#     def test_post_delete(self):
#         self.client.login(username="testuser", password="password")
#         response = self.client.post(
#             reverse("post_delete", kwargs={"slug": self.post.slug})
#         )
#         self.assertRedirects(response, reverse("post_list"))
#         self.assertFalse(Post.objects.filter(slug=self.post.slug).exists())

#     def test_post_publish(self):
#         self.client.login(username="testuser", password="password")
#         response = self.client.post(
#             reverse("post_publish", kwargs={"slug": self.draft_post.slug})
#         )
#         self.assertRedirects(
#             response, reverse("post_detail", kwargs={"slug": self.draft_post.slug})
#         )
#         self.draft_post.refresh_from_db()
#         self.assertIsNotNone(self.draft_post.published_at)

#     def test_post_unpublish(self):
#         self.client.login(username="testuser", password="password")
#         response = self.client.post(
#             reverse("post_unpublish", kwargs={"slug": self.post.slug})
#         )
#         self.assertRedirects(
#             response, reverse("post_detail", kwargs={"slug": self.post.slug})
#         )
#         self.post.refresh_from_db()
#         self.assertIsNone(self.post.published_at)
