from django.db import models

class Note(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=25)
    content = models.TextField(null=True, blank=True)
    date = models.DateField()