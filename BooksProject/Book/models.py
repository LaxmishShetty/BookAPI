from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=50)


class Books(models.Model):
    name = models.CharField(max_length=40)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Readers(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Books)

    def __str__(self):
        return self.name
