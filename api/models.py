from django.db import models

class FavoriteQuote(models.Model):
    text = models.CharField(max_length=255)  # The quote's text
    author = models.CharField(max_length=100, blank=True, null=True)  # The author of the quote
    created_at = models.DateTimeField(auto_now_add=True)  # The timestamp when the quote was added

    def __str__(self):
        return f'"{self.text}" by {self.author or "Unknown"}'

