from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    LINK_TYPES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )

    link = models.URLField()
    work_type = models.CharField(choices=LINK_TYPES, max_length=2)

    def __str__(self):
        return self.link

class Artist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)

    def __str__(self):
        return self.name
