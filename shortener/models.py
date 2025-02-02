from django.db import models

# Create your models here.
class URLMapping(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    access_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.original_url
    
