from django.db import models
from course.models import Course
# from class.models import Class


# Create your models here.
class Student(models.Model):
    # classes = models.OneToOneField(Class, on_delete = models.CASCADE)
    # MANY TO MANY REALTIONSHIP.
    # classes = models.ManyToManyField(Class)
    
    course = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length = 20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    # hospital_report = models.ImageField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
