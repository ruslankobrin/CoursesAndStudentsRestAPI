from django.shortcuts import render
from rest_framework import viewsets

from student_course.models import Course
from student_course.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = [
        "get",
    ]
