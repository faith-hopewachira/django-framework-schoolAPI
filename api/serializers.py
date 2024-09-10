from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classes.models import Class
from classPeriod.models import ClassPeriod
from datetime import date, datetime


class StudentSerializer(serializers.ModelSerializer):
    # teacher = TeacherSerializer()
    class Meta:
        model = Student
        fields = "__all__"

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f'{object.first_name} {object.last_name}'

    # age=serializers.SerializerMethodField()
    # def get_age(self,object):
    #     today = datetime.now
    #     age = today-object.date_of_birth
    #     return age
        
    class Meta:
        model = Student
        fields = ["id","email","full_name"]

class ClassPeriodSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = ClassPeriod
        fields = "__all__"

class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    total_hour_per_course=serializers.SerializerMethodField()
    def get_total_hour_per_course(self,object):
        return f'{object.start_time} to {object.end_time}'
    
    class Meta:
        model = ClassPeriod
        fields = ["id","course","total_hour_per_course"]

class TeacherSerializer(serializers.ModelSerializer):
    # course= CourseSerializer()
    class Meta:
        model = Teacher
        fields = "__all__"

class MinimalTeacherSerializer(serializers.ModelSerializer):
    teacher_full_names=serializers.SerializerMethodField()
    def get_teacher_full_names(self,object):
        return f'{object.first_name} {object.last_name}'
    
    class Meta:
        model = Teacher
        fields = ["id","email","teacher_full_names"]

class CourseSerializer(serializers.ModelSerializer):
    teacher=TeacherSerializer()
    class Meta:
        model = Course
        fields = "__all__"

class MinimalCourseSerializer(serializers.ModelSerializer):
    courses=serializers.SerializerMethodField()
    def get_courses(self,object):
        return f'{object.course_name} {object.course_department}'

class ClassSerializer(serializers.ModelSerializer):
    teacher=TeacherSerializer()
    class Meta:
        model = Course
        fields = "__all__"

class MinimalClassSerializer(serializers.ModelSerializer):
    class_performance=serializers.SerializerMethodField()
    def get_class_performance(self,object):
        return f'{object.class_name} {object.general_performance}'
    
    class Meta:
        model = Class
        fields = ["id","class_status","class_performance"]