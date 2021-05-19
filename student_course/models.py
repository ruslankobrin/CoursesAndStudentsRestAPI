from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)


class CourseParticipant(models.Model):
    class Meta:
        unique_together = [
            "course",
            "student",
        ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    completed = models.BooleanField()
