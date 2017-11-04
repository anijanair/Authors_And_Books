from django.db import models

# Create model for author


class Author(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()


def __str__(self):
    return self.name