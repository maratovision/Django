from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)