from django.db import models

# Create your models here.
class Teacher(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField(max_length = 20)
    nationality = models.CharField(max_length = 20)
    course = models.CharField(max_length = 30)
    teacher_id = models.PositiveSmallIntegerField()
    account_number = models.CharField(max_length = 40)
    date_of_joining = models.DateField()
    gender = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

        