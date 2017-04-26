from __future__ import unicode_literals

from django.db import models

"""
Root User =
user: root
email: root@nativapps.com
password: institucion

Standar User =
user: standar
password: institucion
"""

# Create your models here.
class ParentUser(models.Model):
    identification = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


class Student(ParentUser):
    parent = models.CharField(max_length=100)


class Instructor(ParentUser):
    specialty = models.CharField(max_length=100)


class Grade(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
