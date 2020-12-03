from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from.serializer import ShortenerSerializer
from .models import Shortener


class ShortenerViewSet(viewsets.ModelViewSet):
    serializer_class = ShortenerSerializer
    queryset = Shortener.objects.all()