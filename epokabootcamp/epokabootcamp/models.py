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


class Course(models.Model):
  name = models.CharField(max_length=100)
  department = models.CharField(max_length=100)
  credits = models.IntegerField()
  is_active = models.BooleanField()

  def __str__(self):
    return self.name+" ("+self.department+")"