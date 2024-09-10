from django.db import models
from teacher.models import Teacher
from django.views import View
from django.http import JsonResponse


# Create your models here.
class ClassPeriod(models.Model):
    teacher_first_name = models.ManyToManyField(Teacher)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length = 20)
    classroom = models.CharField(max_length = 20)
    date_of_the_week = models.DateField()

    def __str__(self):
        return f"{self.start_time} {self.end_time}"



class WeeklyTimetableView(View):
    def get(self, request, *args, **kwargs):
        # Query the class periods and serialize them
        periods = ClassPeriod.objects.all()
        timetable = {}
        
        # Organize periods by day_of_week
        for period in periods:
            day = period.day_of_week
            if day not in timetable:
                timetable[day] = []
            timetable[day].append({
                'period_number': period.period_number,
                'teacher': str(period.teacher),
                'course': str(period.course)
            })
        
        return JsonResponse(timetable)