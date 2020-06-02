from django.shortcuts import render
from rest_framework import viewsets
from .models import Books,Genre,Readers
from .serializers import BooksSerializer,GenreSerializer,ReadersSerializer


class BooksView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReadersView(viewsets.ModelViewSet):
    queryset = Readers.objects.all()
    serializer_class = ReadersSerializer

