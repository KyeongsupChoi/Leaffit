# -*- encoding: utf-8 -*-

# Create your models here.
from django.db import models


class RepMax(models.Model):
    weight = models.IntegerField(max_length=200)

    def __str__(self):
        return self.title
