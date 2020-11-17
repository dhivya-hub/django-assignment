from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=True)


class Subject(models.Model):
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.subject


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.user.username
