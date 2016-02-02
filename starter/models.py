from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.CharField(primary_key = True, unique = True, max_length = 200)
    title = models.CharField(max_length = 200)
    year = models.DateField()
    mpaa_rating = models.CharField(max_length = 100)
    runtime = models.IntegerField(default = 0)
    synopsis = models.CharField(max_length = 1000)
    def __unicode__(self):
        return "Title: " + self.title

class ReleaseDate(models.Model):
    movie = models.ForeignKey(Movie)
    theater = models.CharField(max_length = 200)
    date = models.DateField()

class Actor(models.Model):
    id = models.CharField(primary_key = True, unique = True, max_length = 200)
    name = models.CharField(max_length = 200)
    def __unicode__(self):
        return "Name: " + self.name

class Poster(models.Model):
    movie = models.ForeignKey(Movie)
    type = models.CharField(max_length = 200)
    link = models.CharField(max_length = 800)

class Rating(models.Model):
    movie = models.ForeignKey(Movie)
    critics_rating = models.CharField(max_length = 1000)
    critics_score = models.IntegerField(default=0)
    audience_score = models.IntegerField(default=0)

class Character(models.Model):
    movie = models.ForeignKey(Movie)
    actor = models.ForeignKey(Actor)
    name = models.CharField(max_length = 200)

class AlternateID(models.Model):
    movie = models.ForeignKey(Movie)
    type = models.CharField(max_length = 200)
    link = models.CharField(max_length = 800)

class User(models.Model):
    name = models.CharField(max_length = 200)
    role = models.CharField(max_length = 200)

class Recommendation(models.Model):
    from_user = models.ForeignKey(User, related_name='sender_name')
    to_user = models.ForeignKey(User, related_name='receiver_name')
    movie = models.ForeignKey(Movie)