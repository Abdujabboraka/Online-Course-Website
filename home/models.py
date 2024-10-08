from django.db import models


# Course model
class Course(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=8)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Student model
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    reg_date = models.DateField(auto_now_add=True)
    courses = models.ManyToManyField(Course, related_name='students', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
