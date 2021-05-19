from rest_framework import serializers

from student_course.constants import COUNT_PARTICIPANTS
from student_course.models import Student, CourseParticipant, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
        ]


class CourseParticipantSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = CourseParticipant
        fields = [
            "student",
        ]


class CourseSerializer(serializers.ModelSerializer):
    students_count = serializers.SerializerMethodField(read_only=True)
    participants = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            "name",
            "start_date",
            "end_date",
            "students_count",
            "participants",
        ]

    def get_participants(self, obj):
        queryset = CourseParticipant.objects.all().filter(course=obj)[:COUNT_PARTICIPANTS]
        serializer = CourseParticipantSerializer(queryset, many=True)
        return serializer.data

    def get_students_count(self, obj):
        return len(self.get_participants(obj))
