from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
