from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    def __str__(self):
        return self.post_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    post_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class postContent(models.Model):

    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content_text = models.TextField()
