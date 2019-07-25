from django.db import models

# Create your models here.
# id
# title
# poster_path
# overview
# logo_path
# name
# vote_count
# vote_average
# genres :[{"id":18,"name":"Drama"}]

class movieList(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    vote_count = models.IntegerField()
    vote_average = models.IntegerField()
    poster_path = models.URLField()
    logo_path = models.URLField()
    name = models.CharField(max_length=100)