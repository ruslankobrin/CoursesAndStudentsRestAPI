from django.shortcuts import render
from rest_framework import viewsets

from student_course.models import Course, CourseParticipant
from student_course.serializers import CourseSerializer, CourseParticipantSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = [
        "get",
    ]


class CourseParticipantViewSet(viewsets.ModelViewSet):
    queryset = CourseParticipant.objects.all()
    serializer_class = CourseParticipantSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "delete",
    ]
