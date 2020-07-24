from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=8000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
