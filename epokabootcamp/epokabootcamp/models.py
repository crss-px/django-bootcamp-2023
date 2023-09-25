from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=255)
  surname = models.CharField(max_length=255)
  school = models.CharField(max_length=255)