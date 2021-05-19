from django.urls import path, include
from rest_framework import routers

from student_course.views import CourseViewSet, CourseParticipantViewSet, get_csv_report

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'course_patisipants', CourseParticipantViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('get_csv_report/', get_csv_report),
]
