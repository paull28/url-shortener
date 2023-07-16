from django.db import models

# Create your models here.
class url(models.Model):
    new = models.CharField(max_length=255) #New redirect URL
    source = models.CharField(max_length=255) #Original/source URL

    def __str__(self):
        return ("New URL: " + self.new + "\nOriginal URL: " + self.source)
