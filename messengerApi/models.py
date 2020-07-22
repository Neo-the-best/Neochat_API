from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    ava = models.ImageField(null=True, blank=True)
    status = models.TextField()
    country = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    subscriptionsStatus = models.BooleanField()
    friendsCount = models.IntegerField()
    subscribersCount = models.IntegerField()
    photosCount = models.IntegerField()
    audiosCount = models.IntegerField()
