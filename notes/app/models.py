from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Notes(models.Model):

    event = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField()


    def __str__(self):
        return self.event

