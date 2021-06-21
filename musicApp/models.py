from django.db import models

genre_choices = "Rock, Alt, Pop, Jazz, Blues, Hip Hop, Rap"

# Create your models here.
class mainForm(models.Model):
    album_name = models.CharField(max_length=255)
    artist_name = models.CharField(null=True, blank=True, max_length=300)
    genre = models.CharField(max_length=100)