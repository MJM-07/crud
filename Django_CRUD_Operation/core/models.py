from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.IntegerField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return f"{self.student_id} - {self.full_name}"