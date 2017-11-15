from django.db import models


# Model for author

class Author(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.name

# Model for Book

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    review = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    author = models.ForeignKey(Author)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.title

