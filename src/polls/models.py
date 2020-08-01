from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length = 120)
    description = models.TextField(default = 'description default text')

    def __unicode__(self):
        return self.name
"""
class ebaySearch(models.Model):
    searchQuery = models.CharField(max_length = 32)
    #rating = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add = True)

class ebayResults(models.Model):
    rating = models.FloatField()
"""
