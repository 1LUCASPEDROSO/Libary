from django.db import models

class Category(models.Model):
    name = models.CharField(max_length= 100, null=False, blank=False)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, null=False, blank=True)
    description = models.TextField()
    author = models.CharField(max_length= 200)
    release_date = models.CharField(max_length=12 ,null=True, blank=True)
    categorys = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return self.title
