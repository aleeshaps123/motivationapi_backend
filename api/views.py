from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import FavoriteQuote  # Change to the new model
from .serializers import FavoriteQuoteSerializer  # This serializer needs to be created

class FavoriteQuoteListCreate(generics.ListCreateAPIView):
    queryset = FavoriteQuote.objects.all()
    serializer_class = FavoriteQuoteSerializer
    permission_classes = [permissions.AllowAny]

class FavoriteQuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavoriteQuote.objects.all()
    serializer_class = FavoriteQuoteSerializer
    permission_classes = [permissions.AllowAny]

class FavoriteQuoteViewSet(viewsets.ModelViewSet):
    queryset = FavoriteQuote.objects.all()
    serializer_class = FavoriteQuoteSerializer
    permission_classes = [permissions.AllowAny]
