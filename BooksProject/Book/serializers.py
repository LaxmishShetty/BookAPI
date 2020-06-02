from rest_framework import serializers
from .models import Books, Readers, Genre


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('id','url', 'name', 'genre')


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'url', 'name')


class ReadersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Readers
        fields = ('id', 'url', 'name', 'books')