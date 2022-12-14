from email.policy import default
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'published'),
    )
    title =models.CharField(max_length = 250)
    slug = models.CharField(max_length = 250)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                            related_name='blog_posts')
    body = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')


    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return self.title