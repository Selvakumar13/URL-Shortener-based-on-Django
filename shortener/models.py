from django.db import models

class URLMapping(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    full_short_url = models.URLField(null=True, blank=True)  # New field to store the full short URL
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_short_url or self.short_url} -> {self.original_url}"
