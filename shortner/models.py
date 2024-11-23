from django.db import models
import random
import string
from django.utils import timezone

class ShortenedURL(models.Model):
    url = models.URLField(max_length=1024)  # To store the original URL
    shortCode = models.CharField(max_length=6, unique=True)  # Shortened code for the URL
    createdAt = models.DateTimeField(default=timezone.now)  # Time when the shortened URL was created
    updatedAt = models.DateTimeField(auto_now=True)  # Time when the shortened URL was last updated
    accessCount = models.IntegerField(default=0)  # Number of times the short URL is accessed

    def __str__(self):
        return f"{self.shortCode} - {self.url}"


    def save(self, *args, **kwargs):
        """
        Override the default save method to automatically generate a short code 
        when a new ShortenedURL object is created. If the shortCode is not provided, 
        a new code will be generated before saving the object to the database.
        """
        if not self.shortCode:
            self.shortCode = self.generate_short_code()
        if not self.createdAt:
            self.createdAt = timezone.now()
        super(ShortenedURL, self).save(*args, **kwargs)


    def generate_short_code(self):
        """Generate a random short code for the URL."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
