from django.db import models

class Choice(models.Model):
    field_name = models.CharField(max_length=100)

    value = models.CharField(max_length=100)

