# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Email_details(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()

def __str__(self):
        return self.name