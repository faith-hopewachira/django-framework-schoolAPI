from django.urls import path
from .views import StudentListView
from .views import ClassListView
from .views import CourseListView
from .views import TeachersListView
from .views import StudentDetailView
from .views import TeacherDetailView
from .views import CourseDetailView
from .views import ClassPeriodDetailView
from .views import ClassPeriodListView
from .views import ClassDetailView
from .views import ClassListView


urlpatterns = [
    path("students/", StudentListView.as_view(),name="student_list_view"),
    path("classes_school/", ClassListView.as_view(),name="class_list_view"),
    path("teacher/", TeachersListView.as_view(), name= "teacher_list_view"),
    path("course/", CourseListView.as_view(), name="course_list_view"),
    path("classPeriod/", ClassPeriodListView.as_view(), name="class_period_list_view"),
    path("students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),
    path("teacher/<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view"),
    path("course/<int:id>/", CourseDetailView.as_view(), name="course_detail_view"),
    path("classPeriod/<int:id>/", ClassPeriodDetailView.as_view(), name="class_period_detail_view"),
    path("classes/<int:id>/", ClassDetailView.as_view(), name="classes_detail_view"),
    path("classes/", ClassListView.as_view(),name="classes_list_view"),





    

]