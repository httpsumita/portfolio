from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    STATUS_CHOICES = [
        (0, 'Draft'),
        (1, 'Published'),
    ]

    # Fields
    id = models.AutoField(primary_key=True)  # Automatically generated unique ID
    title = models.CharField(max_length=200)  # Title of the blog post
    subtitle = models.CharField(max_length=300, blank=True, null=True)  # Optional subtitle
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # Author of the post
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_on = models.DateTimeField(auto_now=True)  # Timestamp when last updated
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')  # Draft or Published
    likes_count = models.PositiveIntegerField(default=0)  # Likes count, defaults to 0

    def __str__(self):
        return self.title

class Comment(models.Model):
    # Fields for comments
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')  # Linked blog post
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who commented
    content = models.TextField()  # Comment content
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp for comment creation

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog_post.title}"
