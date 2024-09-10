from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from .serializers import ClassPeriodSerializer
from .serializers import TeacherSerializer
from teacher.models import Teacher
from course.models import Course
from classes.models import Class
from classPeriod.models import ClassPeriod
from rest_framework import status
from .serializers import CourseSerializer
from .serializers import ClassSerializer
# from django.http import JsonResponse
from .serializers import MinimalStudentSerializer
from .serializers import MinimalClassPeriodSerializer
from .serializers import MinimalTeacherSerializer
from .serializers import MinimalClassSerializer



# Create your views here.
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name = first_name)
        country = request.query_params.get("country")
        if country:
            students = students.filter(country = country)
        serializer = StudentSerializer(students, many=True)
        serializer = MinimalStudentSerializer(students, many = True)
        return Response(serializer.data)
        # FILTERING
        # CHECKING IF PARAMETERS EXISTS
        # first_name= request.query_params.get("first_name")
        # country= request.query_params.get("country")

        # if first_name:
        #     students = students.filter(first_name=first_name)
        
        # if country:
        #     students = students.filter(country=country)

        # serializer=StudentSerializer(students, many=True)
        # return Response(serializer.data)


    #     # SERIALIZING IT TO JSON FORMAT
    #     serializer = StudentSerializer(students, many = True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # DESERIALIZING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassListView(APIView):
    def get(self, request):
        classes = Class.objects.all()
        serializer=MinimalClassSerializer(classes, many=True)
        return Response(serializer.data) 


    def post(self, request):
        serializer = ClassSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # DESERIALIZING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeachersListView(APIView):
    # def get(self, request):
    #     teacher = Teacher.objects.all()
    #     serializer = TeacherSerializer(teacher, many = True)
    #     return Response(serializer.data)

    def get(self, request):
        teacher = Teacher.objects.all()
        serializer=MinimalTeacherSerializer(teacher, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # DESERIALIZING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = MinimalCourseSerializer(course, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # DESERIALIZING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
class ClassPeriodListView(APIView):
    # def get(self, request):
    #     classPeriod = ClassPeriod.objects.all()
    #     serializer = ClassPeriodSerializer(classPeriod, many = True)
    #     return Response(serializer.data)
    def get(self, request):
        classPeriod = ClassPeriod.objects.all()
        serializer=MinimalClassPeriodSerializer(classPeriod, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # DESERIALIZING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GETTING THE DETAILS OF A USER
class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)



    def put(self, request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ENROLLING A STUDENT TO A COURSE
    def enroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.course.add(course)

    def leave(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.course.remove(course)

    def post(self, request, id):
        student=Student.objects.get(id=id)
        action = request.data.get("action")
        if action=="enroll":
            course_id = request.data.get("course_id")
            self.enroll(student, course_id)
        if action=="leave":
            course_id=request.data.get("course_id")
            self.leave(student, course_id)
        return Response(status=status.HTTP_201_CREATED)

    # ENROLLING A STUDENT TO A CLASS
    def enroll(self, student, class_id):
        classs = Class.objects.get(id=class_id)
        student.classes.add(classes)


class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    # ENROLLING A TEACHER TO A COURSE
    def enroll(self, teacher, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        teacher.course.add(course)


    def leave(self, teacher, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        teacher.course.remove(course)


    def post(self, request, id):
        teacher=Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action=="enroll":
            teacher_id = request.data.get("teacher_id")
            self.enroll(teacher, teacher_id)
        if action=="leave":
            teacher_id=request.data.get("teacher_id")
            self.leave(teacher, teacher_id)
        return Response(status=status.HTTP_201_CREATED)


class ClassPeriodDetailView(APIView):
    def get(self,request,id):
        classPeriod = ClassPeriod.objects.get(id = id)
        serializer = ClassPeriodSerializer(classPeriod)
        return Response(serializer.data)



class StudentDetailView(APIView):
    def put(self, request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class TeacherDetailView(APIView):
    def put(self, request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class CourseDetailView(APIView):
    def put(self, request, id):
        course = Course.objects.get(id = id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class StudentDetailView(APIView):
    def delete(self, request, id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class TeacherDetailView(APIView):
    def delete(self, request, id):
        teacher = Teacher.objects.get(id = id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class CourseDetailView(APIView):
    def delete(self, request, id):
        course = Course.objects.get(id = id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class ClassDetailView(APIView):
    def delete(self, request, id):
        classes = Class.objects.get(id = id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


def weekly_timetable(request):
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



    