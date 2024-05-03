from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    release_year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.title
