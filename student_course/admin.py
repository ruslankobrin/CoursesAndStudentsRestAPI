from django.contrib import admin

from student_course.models import Course, Student, CourseParticipant

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(CourseParticipant)
