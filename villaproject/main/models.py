from django.conf.app_template import models
from django.db import models

class Community(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)


# Create your models here.
