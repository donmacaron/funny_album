from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=150)

    def __str__(self):
        return self.name