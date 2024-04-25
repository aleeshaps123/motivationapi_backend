from rest_framework import serializers
from .models import FavoriteQuote

class FavoriteQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteQuote
        fields = ['id', 'text', 'author', 'created_at']  # Include all necessary fields
