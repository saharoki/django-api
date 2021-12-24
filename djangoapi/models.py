from django.db import models


class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    release_date = models.DateField()
    overview = models.TextField()
    image = models.BinaryField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)