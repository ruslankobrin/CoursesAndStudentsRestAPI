import csv

from django.http import HttpResponse
from rest_framework import viewsets

from student_course.models import Course, CourseParticipant, Student
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


def get_csv_report(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="report.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(
        [
            "Student full name",
            "Number of assigned courses to student",
            "Number of completed courses by student",
        ]
    )
    students = Student.objects.all()

    for student in students:
        num_courses = len(CourseParticipant.objects.filter(student=student))
        num_courses_completed = len(
            CourseParticipant.objects.filter(student=student, completed=True)
        )

        writer.writerow(
            [
                student.first_name + " " + student.last_name,
                num_courses,
                num_courses_completed,
            ]
        )

    return response
