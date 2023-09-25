from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=255)
  surname = models.CharField(max_length=255)
  school = models.CharField(max_length=255)

  def __str__(self):
    if self.school:
      return self.name + " " + self.surname + " (" + self.school + ")"
    else:
      return self.name + " " + self.surname