from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    published_on = models.DateField()